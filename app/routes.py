from fastapi import APIRouter, Header
from app.database import SessionLocal
from app.models import Batch, BatchItem
from app.tasks import analyze_text

router = APIRouter()

@router.post("/batches")
def create_batch(
    items: list[str],
    x_tenant_id: str = Header(...)
):
    db = SessionLocal()

    batch = Batch(
        tenant_id=x_tenant_id,
        status="processing"
    )

    db.add(batch)
    db.commit()
    db.refresh(batch)

    for text in items:

        item = BatchItem(
            batch_id=batch.id,
            text=text,
            status="processing"
        )

        db.add(item)
        db.commit()
        db.refresh(item)

        try:
            result = analyze_text(text)

            item.result = str(result)
            item.status = "completed"

        except Exception as e:
            item.error = str(e)
            item.status = "failed"

        db.commit()

    return {
        "batch_id": batch.id
    }


@router.get("/batches/{batch_id}")
def batch_status(batch_id: int):

    db = SessionLocal()

    items = db.query(BatchItem).filter(
        BatchItem.batch_id == batch_id
    ).all()

    total = len(items)

    done = len([
        i for i in items if i.status == "completed"
    ])

    failed = len([
        i for i in items if i.status == "failed"
    ])

    status = "processing"

    if done == total:
        status = "completed"

    elif failed > 0:
        status = "partially_failed"

    return {
        "total": total,
        "done": done,
        "failed": failed,
        "status": status
    }


@router.get("/batches/{batch_id}/results")
def results(batch_id: int):

    db = SessionLocal()

    items = db.query(BatchItem).filter(
        BatchItem.batch_id == batch_id,
        BatchItem.status == "completed"
    ).all()

    return items


@router.get("/batches/{batch_id}/failures")
def failures(batch_id: int):

    db = SessionLocal()

    items = db.query(BatchItem).filter(
        BatchItem.batch_id == batch_id,
        BatchItem.status == "failed"
    ).all()

    return items
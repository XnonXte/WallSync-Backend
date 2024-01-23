from datetime import datetime

from flask import Blueprint, request

bp = Blueprint("wallpapers", __name__)


@bp.get("/")
def get_all_wallpapers():
    bp.sqlite3_interface.exec_query(
        "CREATE TABLE IF NOT EXISTS wallpapers (id INTEGER, name TEXT, url TEXT, created INTEGER, updated INTEGER, PRIMARY KEY(id))"
    )
    rows = bp.sqlite3_interface.exec_query("SELECT * FROM wallpapers").fetchall()

    return rows


@bp.get("/<int:id>")
def get_wallpaper(id):
    row = bp.sqlite3_interface.exec_query(
        "SELECT * FROM wallpapers WHERE id = ?", (id,)
    ).fetchall()

    return row


@bp.post("/new")
def add_wallpaper():
    name = request.json["name"]
    url = request.json["url"]
    created_timestamp = int(datetime.now().timestamp())

    row_id = bp.sqlite3_interface.exec_query(
        "INSERT INTO wallpapers (name, url, created) VALUES (?, ?, ?)",
        (name, url, created_timestamp),
    ).lastrowid

    if row_id != 0:
        return {"acknowledged": True}
    else:
        return {"acknowledged": False}


@bp.patch("/<int:id>")
def update_wallpaper(id):
    name = request.json["name"]
    url = request.json["url"]
    updated_timestamp = int(datetime.now().timestamp())

    row_count = bp.sqlite3_interface.exec_query(
        "UPDATE wallpapers SET name = ?, url = ?, updated = ? WHERE id = ?",
        (name, url, updated_timestamp, id),
    ).rowcount

    if row_count != 0:
        return {"acknowledged": True}
    else:
        return {"acknowledged": False}


@bp.delete("/<int:id>")
def delete_wallpaper(id):
    row_count = bp.sqlite3_interface.exec_query(
        "DELETE FROM wallpapers WHERE id = ?", (id,)
    ).rowcount

    if row_count != 0:
        return {"acknowledged": True}
    else:
        return {"acknowledged": False}

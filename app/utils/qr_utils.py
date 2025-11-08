import qrcode
import os

def make_qr(udi: str, out_dir: str = "qrs"):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"{udi}.png")
    img = qrcode.make(udi)
    img.save(path)
    return path

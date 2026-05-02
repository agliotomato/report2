from PIL import Image, ImageDraw, ImageFont
import os

REPO = os.path.dirname(os.path.abspath(__file__))

def p(path):
    return os.path.join(REPO, path)

best20 = [
    ("unbraid", "CM_1145",  "+0.0829", "0.5741", "10.67", "0.3185", "0.6570", "15.37", "0.2527"),
    ("unbraid", "CM_1109",  "+0.0769", "0.6001", "12.67", "0.3101", "0.6769", "13.94", "0.2549"),
    ("unbraid", "CM_1206",  "+0.0761", "0.5425", "10.36", "0.3107", "0.6186", "13.75", "0.2527"),
    ("unbraid", "CM_1079",  "+0.0678", "0.5848", "11.23", "0.3021", "0.6526", "15.13", "0.2416"),
    ("unbraid", "CM_1020",  "+0.0673", "0.5995", "11.16", "0.2964", "0.6668", "14.36", "0.2273"),
    ("unbraid", "CM_1040",  "+0.0634", "0.5570", "10.92", "0.3122", "0.6203", "13.22", "0.2463"),
    ("unbraid", "CM_1111",  "+0.0624", "0.5988", "10.45", "0.3368", "0.6612", "14.35", "0.2775"),
    ("unbraid", "CM_1153",  "+0.0611", "0.4985", "10.64", "0.3875", "0.5595", "13.42", "0.3722"),
    ("unbraid", "CM_1029",  "+0.0610", "0.5708", "12.04", "0.2654", "0.6318", "14.37", "0.1976"),
    ("unbraid", "CM_1053",  "+0.0603", "0.6283", "10.10", "0.2569", "0.6886", "12.59", "0.1784"),
    ("unbraid", "CM_1146",  "+0.0579", "0.6621", "10.03", "0.2389", "0.7200", "13.05", "0.2189"),
    ("braid",   "braid_4261","+0.0570","0.5192",  "8.50", "0.4094", "0.5761", "11.58", "0.3476"),
    ("unbraid", "CM_1125",  "+0.0561", "0.6862", "12.23", "0.2378", "0.7423", "14.35", "0.2051"),
    ("unbraid", "CM_1117",  "+0.0559", "0.5510",  "8.92", "0.3307", "0.6069", "11.68", "0.2762"),
    ("unbraid", "CM_1142",  "+0.0545", "0.5181", "11.82", "0.3799", "0.5726", "12.66", "0.3320"),
    ("unbraid", "CM_1200",  "+0.0544", "0.7492", "11.08", "0.2111", "0.8036", "15.13", "0.1816"),
    ("unbraid", "CM_1159",  "+0.0536", "0.6472", "11.66", "0.2636", "0.7008", "15.44", "0.2165"),
    ("unbraid", "CM_1082",  "+0.0529", "0.4263", "11.18", "0.3661", "0.4793", "12.87", "0.3307"),
    ("unbraid", "CM_1080",  "+0.0529", "0.6259", "11.60", "0.3256", "0.6788", "13.99", "0.2870"),
    ("unbraid", "CM_1055",  "+0.0526", "0.6082",  "8.80", "0.3086", "0.6608", "10.71", "0.2290"),
]

worst20 = [
    ("unbraid", "CM_1140",  "-0.0264", "0.6078", "11.30", "0.3169", "0.5814", "10.83", "0.2820"),
    ("unbraid", "R2_1312",  "-0.0258", "0.6371", "10.75", "0.2987", "0.6113", "12.31", "0.3009"),
    ("unbraid", "CM_1197",  "-0.0233", "0.6395",  "9.63", "0.3007", "0.6162",  "9.64", "0.2754"),
    ("unbraid", "wavy_751", "-0.0208", "0.4139", "11.04", "0.4156", "0.3931", "10.02", "0.3952"),
    ("unbraid", "wavy_771", "-0.0203", "0.4366", "11.34", "0.4200", "0.4163", "10.61", "0.4073"),
    ("unbraid", "CM_1012",  "-0.0184", "0.6096",  "9.15", "0.3230", "0.5912",  "8.78", "0.3432"),
    ("unbraid", "CM_1217",  "-0.0178", "0.6707",  "8.78", "0.3298", "0.6529",  "7.84", "0.3147"),
    ("unbraid", "CM_1086",  "-0.0165", "0.6792",  "7.28", "0.3120", "0.6627",  "8.26", "0.3180"),
    ("unbraid", "wavy_761", "-0.0148", "0.4038", "10.03", "0.4349", "0.3890",  "8.52", "0.4431"),
    ("unbraid", "wavy_733", "-0.0144", "0.4616", "10.65", "0.3589", "0.4472", "10.20", "0.3349"),
    ("unbraid", "R2_1793",  "-0.0143", "0.6247", "10.84", "0.3104", "0.6104", "10.93", "0.2646"),
    ("unbraid", "wavy_729", "-0.0139", "0.3220", "10.21", "0.4616", "0.3081",  "9.21", "0.4681"),
    ("unbraid", "wavy_780", "-0.0138", "0.4051", "10.21", "0.4754", "0.3913",  "9.46", "0.4546"),
    ("unbraid", "R2_1168",  "-0.0136", "0.6762",  "9.66", "0.2752", "0.6626",  "9.47", "0.2705"),
    ("unbraid", "wavy_739", "-0.0134", "0.5381", "12.80", "0.3326", "0.5247", "13.65", "0.3109"),
    ("unbraid", "R2_1279",  "-0.0122", "0.5943", "13.03", "0.3048", "0.5821", "13.27", "0.3153"),
    ("unbraid", "CM_1018",  "-0.0120", "0.6218",  "9.81", "0.3207", "0.6097",  "9.51", "0.3087"),
    ("unbraid", "R2_1779",  "-0.0118", "0.7221", "14.19", "0.1798", "0.7104", "15.89", "0.1914"),
    ("unbraid", "wavy_752", "-0.0114", "0.4755", "10.42", "0.3962", "0.4641",  "9.19", "0.3887"),
    ("unbraid", "CM_1028",  "-0.0110", "0.6081",  "6.86", "0.3928", "0.5971",  "7.88", "0.3646"),
]


def get_paths(split, stem):
    sk = p(f"dataset/{split}/sketch/test/{stem}.png")
    gt = p(f"dataset/{split}/img/test/{stem}.png")
    if split == "braid":
        shs = p(f"custom_results/gan/shs/{stem}.png")
        dit = p(f"custom_results/dit/weighted_sum_v4/{stem}_full.png")
    else:
        shs = p(f"custom_results/gan/generated_unbraid/{stem}.png")
        dit = p(f"custom_results/dit/inferunbraidbybraidckp/{stem}_full.png")
    return sk, gt, shs, dit


CELL_W, CELL_H = 256, 256
LABEL_H = 38       # text area below each image
TEXT_ROW_H = 22    # per-row header height
COL_HEADER_H = 28
COLS = 4
ROWS = 20
PAD = 4
BG = (245, 245, 245)
HDR_BG = (50, 50, 50)
HDR_FG = (255, 255, 255)
LABEL_BG = (255, 255, 255)
RANK_BG_BEST  = (220, 240, 220)
RANK_BG_WORST = (240, 220, 220)

try:
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
    font_bold  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 12)
    font_hdr   = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 13)
except Exception:
    font_small = ImageFont.load_default()
    font_bold  = font_small
    font_hdr   = font_small

BLOCK_H = CELL_H + LABEL_H  # height of one image+label block
TOTAL_W = PAD + COLS * (CELL_W + PAD)
TOTAL_H = COL_HEADER_H + ROWS * (BLOCK_H + TEXT_ROW_H + PAD) + PAD


def load_img(path):
    try:
        img = Image.open(path).convert("RGB")
        img = img.resize((CELL_W, CELL_H), Image.LANCZOS)
        return img
    except Exception:
        img = Image.new("RGB", (CELL_W, CELL_H), (200, 200, 200))
        d = ImageDraw.Draw(img)
        d.text((10, CELL_H // 2 - 8), "N/A", fill=(120, 120, 120), font=font_small)
        return img


def draw_text_center(draw, text, x, y, w, h, font, fill=(30, 30, 30)):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((x + (w - tw) // 2, y + (h - th) // 2), text, fill=fill, font=font)


def make_figure(rows_data, title, out_path, rank_bg):
    canvas = Image.new("RGB", (TOTAL_W, TOTAL_H), BG)
    draw = ImageDraw.Draw(canvas)

    # column headers
    col_labels = ["Sketch", "GT", "SHS (GAN)", "DiT v4"]
    for ci, lbl in enumerate(col_labels):
        x = PAD + ci * (CELL_W + PAD)
        draw.rectangle([x, 0, x + CELL_W, COL_HEADER_H], fill=HDR_BG)
        draw_text_center(draw, lbl, x, 0, CELL_W, COL_HEADER_H, font_hdr, HDR_FG)

    y_off = COL_HEADER_H

    for rank, row in enumerate(rows_data, 1):
        split, stem, delta, g_ssim, g_psnr, g_lpips, d_ssim, d_psnr, d_lpips = row
        sk_path, gt_path, shs_path, dit_path = get_paths(split, stem)
        imgs = [load_img(sk_path), load_img(gt_path), load_img(shs_path), load_img(dit_path)]

        # rank / stem / delta header row
        row_lbl = f"#{rank}  {stem}  ΔSSIM {delta}"
        draw.rectangle([PAD, y_off, TOTAL_W - PAD, y_off + TEXT_ROW_H], fill=rank_bg)
        draw_text_center(draw, row_lbl, PAD, y_off, TOTAL_W - 2*PAD, TEXT_ROW_H, font_bold)
        y_off += TEXT_ROW_H

        # images
        for ci, img in enumerate(imgs):
            x = PAD + ci * (CELL_W + PAD)
            canvas.paste(img, (x, y_off))

        # labels below images
        label_texts = [
            "",  # sketch — no metrics
            "",  # GT — no metrics
            f"SSIM {g_ssim}  PSNR {g_psnr}  LPIPS {g_lpips}",
            f"SSIM {d_ssim}  PSNR {d_psnr}  LPIPS {d_lpips}",
        ]
        for ci, txt in enumerate(label_texts):
            x = PAD + ci * (CELL_W + PAD)
            ly = y_off + CELL_H
            draw.rectangle([x, ly, x + CELL_W, ly + LABEL_H], fill=LABEL_BG)
            if txt:
                # two lines
                parts = txt.split("  ")
                line1 = "  ".join(parts[:2])
                line2 = parts[2] if len(parts) > 2 else ""
                b1 = draw.textbbox((0,0), line1, font=font_small)
                b2 = draw.textbbox((0,0), line2, font=font_small)
                tw1 = b1[2]-b1[0]; tw2 = b2[2]-b2[0]
                draw.text((x + (CELL_W - tw1)//2, ly + 4), line1, fill=(40,40,40), font=font_small)
                draw.text((x + (CELL_W - tw2)//2, ly + 18), line2, fill=(40,40,40), font=font_small)

        y_off += BLOCK_H + PAD

    canvas.save(out_path)
    print(f"Saved: {out_path}")


braid_best5 = [
    ("braid", "braid_4261", "+0.0570", "0.5192",  "8.50", "0.4094", "0.5761", "11.58", "0.3476"),
    ("braid", "braid_4315", "+0.0495", "0.4298", "10.55", "0.4726", "0.4793", "12.07", "0.4692"),
    ("braid", "braid_4135", "+0.0477", "0.5108", "11.17", "0.3503", "0.5585", "12.36", "0.3702"),
    ("braid", "braid_4052", "+0.0417", "0.4991", "10.79", "0.4330", "0.5408", "12.28", "0.4058"),
    ("braid", "braid_4138", "+0.0414", "0.5474", "11.25", "0.3628", "0.5889", "12.97", "0.3567"),
]

braid_worst5 = [
    ("braid", "braid_2537", "-0.0080", "0.4269",  "8.87", "0.4529", "0.4189",  "8.47", "0.4708"),
    ("braid", "braid_4201", "-0.0074", "0.6122", "13.78", "0.2947", "0.6048", "13.83", "0.3762"),
    ("braid", "braid_4042", "-0.0069", "0.5659", "10.36", "0.2771", "0.5590", "10.93", "0.2792"),
    ("braid", "braid_3188", "-0.0068", "0.5405",  "9.79", "0.3228", "0.5337",  "9.67", "0.3681"),
    ("braid", "braid_4143", "-0.0049", "0.7238", "11.18", "0.2191", "0.7189", "12.49", "0.2243"),
]

make_figure(best20,      "Best 20 (ΔSSIM)",
            p("custom_results/best20.png"),       RANK_BG_BEST)
make_figure(worst20,     "Worst 20 (ΔSSIM)",
            p("custom_results/worst20.png"),      RANK_BG_WORST)
make_figure(braid_best5, "Braid Best 5 (ΔSSIM)",
            p("custom_results/braid_best5.png"),  RANK_BG_BEST)
make_figure(braid_worst5,"Braid Worst 5 (ΔSSIM)",
            p("custom_results/braid_worst5.png"), RANK_BG_WORST)

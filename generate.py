import os
import glob

dirs = ["滨城", "萌茶", "红龙"]

pre = """# 一个匹兹堡中餐外卖菜品名称-图片数据库

图片取自微信群，由商家提供

"""


def generate_readme():
    content = pre

    for dir_name in dirs:
        if os.path.exists(dir_name) and os.path.isdir(dir_name):
            content += f"## {dir_name}\n\n"

            image_extensions = [
                "*.jpg",
                "*.jpeg",
                "*.png",
                "*.gif",
                "*.bmp",
                "*.webp",
            ]
            image_files = []

            for ext in image_extensions:
                image_files.extend(
                    glob.glob(
                        os.path.join(dir_name, f"**/{ext}"), recursive=True
                    )
                )

            image_files.sort()

            for img_path in image_files:
                filename = os.path.splitext(os.path.basename(img_path))[0]

                content += f"### {filename}\n\n"
                content += f'<img src="{img_path}" alt="{filename}" width="100px" />\n\n'

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

    print("README.md generated successfully!")


if __name__ == "__main__":
    generate_readme()

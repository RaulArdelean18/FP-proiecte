def copy_file_content(src, dst):
    with open(src, "r", encoding="utf-8") as fsrc, open(dst, "w", encoding="utf-8") as fdst:
        fdst.write(fsrc.read())

def clear_file_content(path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("")

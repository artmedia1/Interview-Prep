def convert(s: str):
    s = s.replace(" ", "_")
    s = s.replace(".", "")
    print(s+".py")

if __name__ == "__main__":
    name = "226. Invert Binary Tree"
    convert(name)

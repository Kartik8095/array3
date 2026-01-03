def main():
    scores = [10, 20, 30, 50]
    total = sum(scores)
    average = total / len(scores)

    print("=== main/master branch output ===")
    print(f"Scores = {scores}")
    print(f"Average = {average}")
    
    print("=== local branch output ===")
    print(f"maximum = {max(scores)}")
    print(f"minimum = {min(scores)}")

if __name__ == "__main__":
    main()
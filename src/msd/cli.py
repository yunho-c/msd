"""Command-line interface for MSD dataset tools."""
import kagglehub


def download_dataset():
    """Download the MSD dataset from Kaggle."""
    path = kagglehub.dataset_download("caspervanengelenburg/modified-swiss-dwellings")
    print(f"Path to dataset files: {path}")
    return path


def main():
    """Main entry point for CLI."""
    download_dataset()


if __name__ == "__main__":
    main()

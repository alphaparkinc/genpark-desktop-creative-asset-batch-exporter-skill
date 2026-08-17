from client import DesktopCreativeAssetBatchExporterClient

def main():
    client = DesktopCreativeAssetBatchExporterClient()
    res = client.batch_export_assets("master_hero_banner.png", ["1:1", "9:16", "16:9", "4:5"])
    print(f"Export Duration: {res['export_duration_sec']}s")
    print(f"Files Generated: {res['total_files_generated']}")
    print("Exported Asset URLs:", res["exported_assets_urls"])

if __name__ == "__main__":
    main()

class DesktopCreativeAssetBatchExporterClient:
    def batch_export_assets(self, source_master_asset: str, target_aspect_ratios: list = None) -> dict:
        if target_aspect_ratios is None:
            target_aspect_ratios = ["1:1", "9:16", "16:9"]
        urls = [f"https://cdn.genpark.ai/assets/export_{ratio.replace(':', 'x')}.png" for ratio in target_aspect_ratios]
        return {
            "exported_assets_urls": urls,
            "total_files_generated": len(urls),
            "export_duration_sec": 1.8
        }

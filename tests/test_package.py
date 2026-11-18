import tariff_pricing


def test_package_exposes_version() -> None:
    assert tariff_pricing.__version__ == "0.1.0"

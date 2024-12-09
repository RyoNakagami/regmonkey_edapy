---
author: "Ryo Nakagami"
date-modified: "2024-12-09"
project: regmonkey-edapy
---

## Version policy

`regmonkey-edapy` のversion管理は[semantic versioning](https://semver.org/)に基づいています．

`regmonkey-edapy`  release number は `MAJOR.MINOR.PATCH` から構成されています．

<strong > &#9654;&nbsp; Major release</strong>

- 後方互換性のないbreaking changesが発生した場合，Major releaseとして対応します
- Major releaseに含まれた変更は，Release noteにてdocument化されます
- deprecationsに基づくmethodやattributeの廃止は，Major releaseのみで行われます

<strong > &#9654;&nbsp; Minor release</strong>

- Minor releaseは，大規模なバグ修正や後方互換性を保ちながら追加される新機能（例: 新しいmethodの追加）を加えた場合に行われます
- deprecationsのアナウンスはMinor releaseで実施します(Patch releaseでは導入しない)

deprecationsのアナウンスは以下の２点のガイダンスを含んだ警告として実施します

- 代替手段のアナウンス
- deprecationが強制されるversionのアナウンス

`regmonkey-edapy` `1.2.0`で動作がdeprecationsとなった場合，`1.x` versionの
すべてのリリースで警告付きで引き続き動作します．動作は次のMajor release（`2.0.0`）で変更され，deprecationsは削除されます．

<strong > &#9654;&nbsp; Patch release</strong>

Patch releaseは後方互換性のあるBUG FIXを入れた場合に行われます．後方互換性とは，パッケージバージョンをアップグレードしても， 以前に記述したコードがそのまま動作することを意味します．

## References

- [semantic versioning](https://semver.org/)
- [Python package building techniques for regmonkeys > versioning policy](https://ryonakagami.github.io/python-statisticalpackage-techniques/posts/python-packaging-guide/versioning.html)

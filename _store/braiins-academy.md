---
aid: braiins-academy
url: https://raw.githubusercontent.com/api-evangelist/braiins-academy/refs/heads/main/apis.yml
name: Braiins
tags:
  - Bitcoin Mining
  - Cryptocurrency
  - Mining Pool
  - Mining Firmware
  - Blockchain
  - Stratum V2
type: Index
x-type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-03-01'
modified: '2026-04-21'
position: Consumer
description: Braiins is a Bitcoin mining technology company operating the world's longest-running Bitcoin mining pool (Slush Pool, now Braiins Pool), developing Braiins OS+ mining firmware, and pioneering the Stratum V2 next-generation mining protocol. Braiins Academy provides educational resources on Bitcoin mining, and the company publishes a public Mining Insights API with network statistics. Stratum V2 increases mining security, bandwidth efficiency, and miner autonomy through decentralized transaction selection.
apis:
  - aid: braiins-academy:mining-insights-api
    name: Braiins Mining Insights Public API
    tags:
      - Bitcoin Mining
      - Mining Statistics
      - Network Data
      - Hashrate
    humanURL: https://academy.braiins.com/en/mining-insights/public-api/
    properties:
      - url: https://academy.braiins.com/en/mining-insights/public-api/
        type: Documentation
    description: The Braiins Mining Insights Public API provides access to Bitcoin mining network statistics, hashrate data, and mining pool performance metrics. Used for research, analysis, and integration with mining management tools.
  - aid: braiins-academy:braiins-pool-api
    name: Braiins Pool API
    tags:
      - Mining Pool
      - Bitcoin
      - Hashrate
      - Payouts
    humanURL: https://braiins.com/pool
    properties:
      - url: https://braiins.com/pool
        type: Documentation
    description: API access for Braiins Pool (formerly Slush Pool), the world's first Bitcoin mining pool. Provides miner statistics, payout data, worker management, and pool hashrate information.
  - aid: braiins-academy:braiins-os-api
    name: Braiins OS+ Firmware API
    tags:
      - Mining Firmware
      - ASIC
      - Autotuning
      - Performance
    humanURL: https://braiins.com/os/plus
    properties:
      - url: https://braiins.com/os/plus
        type: Documentation
    description: Braiins OS+ is custom mining firmware for Bitcoin ASICs (Antminer series) featuring autotuning, dynamic performance scaling, and thermal management. Supports remote batch configuration via Braiins Toolbox and integrates with Braiins Pool for 0% effective pool fee.
common:
  - type: Website
    url: https://braiins.com
  - type: Academy
    url: https://academy.braiins.com
  - type: Pool
    url: https://braiins.com/pool
  - type: Firmware
    url: https://braiins.com/os/plus
  - type: StratumV2
    url: https://braiins.com/stratum-v2
  - type: Documentation
    url: https://academy.braiins.com/os/plus-en/
properties:
  - type: x-domain
    value: braiins.com
  - type: x-founded
    value: '2011'
  - type: x-headquarters
    value: Prague, Czech Republic
  - type: x-industry
    value: Bitcoin Mining Technology
  - type: x-products
    value: Braiins Pool, Braiins OS+, Braiins Toolbox, Stratum V2, Braiins Academy
  - type: x-protocol
    value: Stratum V2 - next-generation Bitcoin mining protocol
  - type: x-stratum-v2-features
    value: Enhanced security (prevents MITM attacks and hashrate hijacking), bandwidth efficiency, miner-side transaction selection, decentralization improvement
  - type: x-firmware-features
    value: Autotuning per-chip frequency calibration, dynamic thermal management, overclocking, underclocking, batch remote configuration, 24/7 support
  - type: x-supported-hardware
    value: Antminer S21 series, S19 series, T19, S17 series, S9 series
  - type: x-capabilities
    value: Mining pool management, firmware-based performance optimization, hashrate monitoring, mining network analytics, Stratum V2 protocol implementation
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---

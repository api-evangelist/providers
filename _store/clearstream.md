---
aid: clearstream
url: https://raw.githubusercontent.com/api-evangelist/clearstream/refs/heads/main/apis.yml
name: Clearstream
created: '2024-01-15'
modified: '2026-04-23'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
x-type: company
tags:
  - Capital Markets
  - Collateral Management
  - Custody
  - Financial Services
  - ISO 15022
  - ISO 20022
  - Post-Trade Infrastructure
  - Securities
  - Settlement
  - SWIFT
description: Clearstream is a leading provider of post-trade infrastructure services for international securities transactions. They offer settlement, custody, and collateral management services for bonds, equities, and investment funds. The Clearstream developer surface is built on regulated post-trade messaging rather than a public REST API. Clients connect through ClearstreamXact (Web Portal, File Transfer via SWIFTNet FileAct, and Xact via SWIFT FIN), CASCADE via SWIFT and MQ, the CreationOnline / CreationDirect channels, Vestima for fund order routing, and the CmaX triparty collateral platform. Messages follow ISO 15022 and ISO 20022 standards, with ongoing migration toward ISO 20022 driven by the SWIFT CBPR+ programme.
apis:
  - aid: clearstream:xact-via-swift
    name: Clearstream Xact via SWIFT
    tags:
      - Custody
      - ISO 15022
      - ISO 20022
      - Settlement
      - SWIFT
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.clearstream.com/clearstream-en/securities-services/connectivity-1-/xact-via-swift--1276378
    properties:
      - url: https://www.clearstream.com/clearstream-en/securities-services/connectivity-1-/xact-via-swift--1276378
        type: Documentation
      - url: https://www.clearstream.com/clearstream-en/securities-services/connectivity-1-/xact-via-swift-user-guides-1289256
        type: User Guides
      - url: https://www.clearstream.com/clearstream-en/securities-services/connectivity-1-/swift-mystandards-1277070
        type: SWIFT MyStandards
    description: Xact via SWIFT delivers settlement, custody, asset servicing and reporting messages over the SWIFTNet FIN network. The interface uses ISO 15022 MT messages today and is being migrated to ISO 20022 MX messages in line with the SWIFT CBPR+ schedule. Message specifications are published to SWIFT MyStandards.
  - aid: clearstream:xact-file-transfer
    name: Clearstream Xact File Transfer
    tags:
      - File Transfer
      - ISO 20022
      - SWIFTNet FileAct
      - Settlement
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.clearstream.com/clearstream-en/securities-services/connectivity-1-/xact-file-transfer
    properties:
      - url: https://www.clearstream.com/clearstream-en/securities-services/connectivity-1-/xact-file-transfer
        type: Documentation
      - url: https://www.clearstream.com/clearstream-en/keydocuments-1-/icsd-1-/connectivity-manuals
        type: Connectivity Manuals
    description: Xact File Transfer offers bulk and report-style exchange of settlement, custody, and collateral messages over SWIFTNet FileAct. Files may be delivered in ISO 15022, ISO 20022, PDF, XML or XLS formats and are used for high-volume corporate-action notifications, statements, and bilateral reconciliation.
  - aid: clearstream:xact-web-portal
    name: Clearstream Xact Web Portal
    tags:
      - Asset Servicing
      - Custody
      - Settlement
      - Web Portal
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.clearstream.com/clearstream-en/securities-services/connectivity-1-/clearstreamxact
    properties:
      - url: https://www.clearstream.com/clearstream-en/securities-services/connectivity-1-/clearstreamxact
        type: Documentation
      - url: https://www.clearstream.com/clearstream-en/securities-services/connectivity-1-/clearstreamxact/testing
        type: Testing
    description: Xact Web Portal is the browser-based interface to ClearstreamXact for instructing settlement, custody and collateral activity, monitoring status, and reviewing reports. It complements the SWIFT and FileAct programmatic channels with a manual / four-eyes operator surface.
  - aid: clearstream:cascade
    name: Clearstream CASCADE (CSD)
    tags:
      - CSD
      - Domestic Settlement
      - Germany
      - SWIFT
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.clearstream.com/clearstream-en/securities-services/connectivity-1-/cascade
    properties:
      - url: https://www.clearstream.com/clearstream-en/securities-services/connectivity-1-/cascade
        type: Documentation
      - url: https://www.clearstream.com/clearstream-en/securities-services/connectivity-1-/cascade/cascade-via-swift
        type: CASCADE via SWIFT
    description: CASCADE is the German central securities depository (CSD) settlement platform. CASCADE is reachable via SWIFT FIN/FileAct messages and via MQ-based host-to-host connectivity for instructing domestic and cross-border settlement, corporate actions, and tax services.
  - aid: clearstream:vestima
    name: Clearstream Vestima
    tags:
      - Funds
      - ISO 20022
      - Order Routing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.clearstream.com/clearstream-en/securities-services/funds-services-1-/vestima
    properties:
      - url: https://www.clearstream.com/clearstream-en/securities-services/funds-services-1-/vestima
        type: Documentation
    description: Vestima is Clearstream's investment fund processing platform. It routes subscription, redemption, switch and transfer orders for mutual funds, ETFs, hedge funds and alternatives, and integrates with SWIFT, FIX, and proprietary file transfer for both retail and institutional flows.
  - aid: clearstream:cmax
    name: Clearstream CmaX (Triparty Collateral)
    tags:
      - Collateral Management
      - Margin
      - Triparty
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.clearstream.com/clearstream-en/securities-services/collateral-management
    properties:
      - url: https://www.clearstream.com/clearstream-en/securities-services/collateral-management
        type: Documentation
    description: CmaX is Clearstream's triparty collateral management platform. It automates collateral allocation, optimisation, margining and substitution across repo, securities lending, and OTC derivatives exposures. Clients interact via SWIFT colr.* messages and Xact File Transfer feeds.
common:
  - type: Website
    url: https://www.clearstream.com/
  - type: Portal
    url: https://www.clearstream.com/clearstream-en/products-and-services
  - type: Documentation
    url: https://www.clearstream.com/clearstream-en/keydocuments-1-/icsd-1-/connectivity-manuals
  - type: Support
    url: https://www.clearstream.com/clearstream-en/contact
  - type: Terms of Service
    url: https://www.clearstream.com/clearstream-en/legal-and-regulatory
  - type: JSON-LD
    url: json-ld/clearstream-context.jsonld
  - type: Spectral
    url: rules/clearstream-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/clearstream-post-trade.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

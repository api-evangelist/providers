---
aid: federal-trade-commission
name: Federal Trade Commission
description: The Federal Trade Commission (FTC) is a U.S. federal agency that enforces antitrust and consumer protection laws affecting virtually every area of commerce. The FTC publishes developer-facing data products and APIs through ftc.gov/developer and partner platforms, including the National Do Not Call Registry telemarketer access program and the Consumer Sentinel Network of consumer complaint data shared with law enforcement.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-04-28'
position: Consumer
tags:
  - Antitrust
  - Consumer Protection
  - Do Not Call
  - Federal Government
  - Law Enforcement
  - Open Data
url: https://raw.githubusercontent.com/api-evangelist/federal-trade-commission/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: federal-trade-commission:developer-portal
    name: FTC Developer Portal
    description: The FTC Developer Portal is the central hub for developer documentation, data dictionaries, and access program details for FTC-managed datasets and services.
    humanURL: https://www.ftc.gov/developer
    baseURL: https://api.ftc.gov
    tags:
      - Federal Government
      - Documentation
    properties:
      - type: Documentation
        url: https://www.ftc.gov/developer
      - type: Website
        url: https://www.ftc.gov/
  - aid: federal-trade-commission:do-not-call-registry
    name: National Do Not Call Registry
    description: The National Do Not Call Registry program lets telemarketers and sellers download phone-number data they must scrub against before placing calls. Access is provisioned through telemarketer.donotcall.gov and governed by the Telemarketing Sales Rule.
    humanURL: https://telemarketers.donotcall.gov
    tags:
      - Do Not Call
      - Consumer Protection
      - Telemarketing
    properties:
      - type: Documentation
        url: https://telemarketers.donotcall.gov
      - type: Consumer Site
        url: https://www.donotcall.gov
  - aid: federal-trade-commission:consumer-sentinel
    name: Consumer Sentinel Network
    description: Consumer Sentinel is the FTC's secure online database of consumer reports of fraud, identity theft, and other complaints, made available to participating federal, state, local, and international law enforcement agencies through a vetted access program.
    humanURL: https://www.ftc.gov/enforcement/consumer-sentinel-network
    tags:
      - Consumer Protection
      - Law Enforcement
      - Fraud
    properties:
      - type: Documentation
        url: https://www.ftc.gov/enforcement/consumer-sentinel-network
      - type: Data Book
        url: https://www.ftc.gov/enforcement/consumer-sentinel-network/reports
  - aid: federal-trade-commission:hsr-premerger
    name: HSR Premerger Notification
    description: The Hart-Scott-Rodino (HSR) Premerger Notification Program coordinates premerger filings reviewed by the FTC and DOJ. Filings are submitted electronically through the dedicated HSR e-filing system.
    humanURL: https://www.ftc.gov/enforcement/premerger-notification-program
    tags:
      - Antitrust
      - Mergers
    properties:
      - type: Documentation
        url: https://www.ftc.gov/enforcement/premerger-notification-program
      - type: E-Filing
        url: https://www.hsr.gov
common:
  - type: Website
    url: https://www.ftc.gov/
  - type: Documentation
    url: https://www.ftc.gov/developer
  - type: News
    url: https://www.ftc.gov/news-events
  - type: Open Data
    url: https://www.ftc.gov/policy/research
  - type: Consumer Resources
    url: https://consumer.ftc.gov
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

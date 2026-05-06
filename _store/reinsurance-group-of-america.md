---
aid: reinsurance-group-of-america
name: Reinsurance Group of America
description: Reinsurance Group of America (RGA) is a leading global provider of life and health reinsurance and financial solutions, serving clients in more than 70 countries. RGA is the only global reinsurance company focused exclusively on life and health solutions. The company provides reinsurance, automated underwriting platforms, digital health data scoring, and financial risk management solutions to insurance carriers worldwide.
type: Index
url: https://raw.githubusercontent.com/api-evangelist/reinsurance-group-of-america/refs/heads/main/apis.yml
tags:
  - Financial Services
  - Health Insurance
  - Insurance Technology
  - Life Insurance
  - Reinsurance
  - Underwriting
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: reinsurance-group-of-america:aura-next
    name: AURA NEXT Automated Underwriting API
    description: AURA NEXT is RGA's SaaS-based automated underwriting decision management platform powered by 40+ years of underwriting expertise. The API enables insurance carriers to integrate real-time underwriting decisions, manage and share rule sets, and streamline end-to-end underwriting processes. Supports point-of-sale decisions through integration with call centers, agents, brokers, e-applications, and portals.
    humanURL: https://www.rgare.com/solutions/underwriting/automated-underwriting
    baseURL: https://api.rgare.com/aura
    tags:
      - Automated Underwriting
      - Decision Management
      - Insurance
      - Life Insurance
      - SaaS
      - Underwriting
    properties:
      - type: Documentation
        url: https://www.rgare.com/solutions/underwriting/automated-underwriting
      - type: Website
        url: https://www.rgax.com/life-underwriting/aura-next/
  - aid: reinsurance-group-of-america:digital-health-data
    name: Digital Health Data Risk Scoring API
    description: RGA's Digital Health Data (DHD) Risk Scoring service provides a real-time API for evaluating structured electronic medical record and medical claims data to derive actionable underwriting risk scores. Available for use across a broad range of use cases from triage through post-issue monitoring, enabling carriers to reduce applicant wait times and improve underwriting consistency.
    humanURL: https://www.rgare.com/our-company/media/press-releases/press-releases-detail/2020/02/04/rga-announces-industry-s-first-digital-health-data-scoring-service
    baseURL: https://api.rgare.com/dhd
    tags:
      - Digital Health
      - Electronic Health Records
      - Life Insurance
      - Risk Scoring
      - Underwriting
    properties:
      - type: Documentation
        url: https://www.rgare.com/our-company/media/press-releases/press-releases-detail/2020/02/04/rga-announces-industry-s-first-digital-health-data-scoring-service
      - type: Website
        url: https://investor.rgare.com/news-releases/news-release-details/rga-announces-industrys-first-digital-health-data-scoring
common:
  - type: Website
    url: https://www.rgare.com/
    name: RGA Official Website
  - type: Website
    url: https://www.rgax.com/
    name: RGAX - RGA Innovation Hub
  - type: Documentation
    url: https://www.rgare.com/solutions/all-products-and-services
    name: RGA All Products and Services
  - type: Website
    url: https://investor.rgare.com/
    name: RGA Investor Relations
  - type: Documentation
    url: https://www.rgare.com/knowledge-center
    name: RGA Knowledge Center
  - type: Website
    url: https://en.wikipedia.org/wiki/Reinsurance_Group_of_America
    name: Reinsurance Group of America - Wikipedia
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/reinsurance-group-of-america/refs/heads/main/json-schema/reinsurance-group-of-america-underwriting-decision-schema.json
    name: AURA NEXT Underwriting Decision JSON Schema
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/reinsurance-group-of-america/refs/heads/main/json-schema/reinsurance-group-of-america-health-score-schema.json
    name: Digital Health Data Risk Score JSON Schema
  - type: JSONStructure
    url: https://raw.githubusercontent.com/api-evangelist/reinsurance-group-of-america/refs/heads/main/json-structure/reinsurance-group-of-america-underwriting-decision-structure.json
    name: Underwriting Decision JSON Structure
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/reinsurance-group-of-america/refs/heads/main/json-ld/reinsurance-group-of-america-context.jsonld
    name: Reinsurance Group of America JSON-LD Context
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/reinsurance-group-of-america/refs/heads/main/vocabulary/reinsurance-group-of-america-vocabulary.yml
    name: Reinsurance Group of America Vocabulary
  - type: Examples
    url: https://raw.githubusercontent.com/api-evangelist/reinsurance-group-of-america/refs/heads/main/examples/reinsurance-group-of-america-underwriting-decision-example.json
    name: AURA NEXT Underwriting Decision Example
  - type: Examples
    url: https://raw.githubusercontent.com/api-evangelist/reinsurance-group-of-america/refs/heads/main/examples/reinsurance-group-of-america-health-score-example.json
    name: Digital Health Data Risk Score Example
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

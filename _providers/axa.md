---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/axa-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/axa-group
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/axa
- group: company
  title: ''
  type: Website
  url: https://www.axa.com/
- group: other
  title: ''
  type: GroupSite
  url: https://group.axa.com/
- group: company
  title: ''
  type: Partners
  url: https://www.axapartners.com/
- group: other
  title: ''
  type: AXAXL
  url: https://axaxl.com/
- group: other
  title: ''
  type: Brokers
  url: https://axaxl.com/brokers
- group: other
  title: ''
  type: Suppliers
  url: https://www.axa.com/en/about-us/suppliers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.axa.com/en/page/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.axa.com/en/page/general-terms-and-conditions-of-use
- group: operate
  title: ''
  type: Contact
  url: https://www.axa.com/en/about-us/contact
- group: auth
  title: ''
  type: Compliance
  url: ''
created: '2026-05-05'
description: AXA is a French multinational insurance firm and one of the world's largest providers of life, health, property & casualty, and asset management services. AXA does not publish a single global developer portal; technology integration is delivered through country-specific broker and partner portals, AXA Partners B2B2C distribution channels, AXA XL specialty insurance APIs for commercial brokers, and ACORD / EDI standards used across the insurance industry.
features:
- description: AXA operating entities publish country-specific broker and agent portals (e.g. AXA UK, AXA France, AXA Germany) used for quote, bind, and policy servicing.
  name: Country Broker Portals
- description: AXA Partners offers travel, assistance, and embedded insurance distributed via B2B2C partners through private API integrations.
  name: AXA Partners Embedded Insurance
- description: AXA XL provides commercial property, casualty, marine, and specialty risk capacity through ACORD-aligned broker workflows.
  name: AXA XL Specialty Insurance
- description: Policy, claims, and accounting transactions are exchanged with brokers and reinsurers using ACORD AL3 and ACORD XML standards.
  name: ACORD Messaging
- description: Investor relations, ESG disclosures, and group press releases are published on group.axa.com.
  name: Group Communications
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/axa.png
layout: provider
modified: '2026-05-16'
name: AXA
nav: Providers
network: true
overview: AXA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Financial Services, and Asset Management.
random_paper: 82
score:
  band: emerging
  composite: 13.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 13.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 28.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/axa/refs/heads/main/screenshots/axa-2026-06-20T172806.png
security:
- kind: domain-security
  name: Axa Domain Security
  slug: axa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: axa
tags:
- Insurance
- Financial Services
- Asset Management
use_cases:
- description: Brokers issue quotes, bind policies, and service customers through AXA's country-specific portals and ACORD-aligned channels.
  name: Broker Policy Administration
- description: Banks, telcos, and travel platforms distribute AXA-branded coverage through AXA Partners B2B2C agreements.
  name: Embedded Insurance Distribution
- description: First notice of loss and claims status updates are exchanged with policyholders, brokers, and repair networks.
  name: Claims Notification and Servicing
- description: Treaty and facultative placements with reinsurers use ACORD reinsurance accounting and claims messaging.
  name: Reinsurance and Capacity Placement
- description: AXA publishes climate, biodiversity, and sustainability disclosures aligned with TCFD, CSRD, and SBTi frameworks.
  name: ESG and Sustainability Reporting
website: https://www.axa.com/
---

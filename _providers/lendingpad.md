---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 4
apis:
- description: Modeled loan-file exchange surface - create, read, and update mortgage loan files, submit loan data to lenders/investors, and import/export loan data (LendingPad describes MISMO-style 3.2/3.4 loan-dat
  name: LendingPad Loans API (modeled)
  slug: lendingpad-loans-api
- description: Modeled document and condition exchange surface - push borrower and loan documents into the LendingPad LOS (as POS/doc-prep partners like Floify and DocMagic do) and manage underwriting conditions and
  name: LendingPad Documents & Conditions API (modeled)
  slug: lendingpad-documents-conditions-api
- description: Modeled product, pricing, and eligibility (PPE) exchange surface - integrations with pricing engines such as Polly, Lender Price, Optimal Blue, and LoanNex return real-time product and pricing results
  name: LendingPad Pricing & Product Eligibility API (modeled)
  slug: lendingpad-pricing-eligibility-api
- description: Modeled event/notification surface - partner integrations describe synchronization of field updates, critical dates, and loan-status changes back to external systems (e.g. Shape's bi-directional sync)
  name: LendingPad Webhooks & Events (modeled)
  slug: lendingpad-webhooks-events-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/lendingpad-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lendingpad-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lendingpad.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lendingpad
- group: docs
  title: ''
  type: Documentation
  url: https://lendingpad.com/api-terms
- group: company
  title: ''
  type: PartnerProgram
  url: https://lendingpad.com/partners-marketplace
- group: other
  title: ''
  type: KnowledgeBase
  url: https://kb.lendingpad.com/integrations
- group: company
  title: ''
  type: Blog
  url: https://blog.lendingpad.com
- group: commercial
  title: ''
  type: Plans
  url: plans/lendingpad-plans-pricing.yml
created: '2026-07-04'
description: LendingPad is a cloud-based mortgage loan origination system (LOS) that lets brokers, lenders, and institutions originate, process, underwrite, close, and fund residential mortgage loans with real-time, multi-user collaboration across the borrower, broker, lender, and service-provider lifecycle. It ships in Broker, Lender, Processing, and Institution editions and runs a large Partners Marketplace of integrated vendors (credit, AUS, AVM/appraisal, title, compliance, doc-prep, pricing/PPE, POS, CRM, and investors such as Fannie Mae, Freddie Mac, UWM, and Rocket Mortgage). LendingPad exposes an Enterprise API for loan data exchange, but access is gated - it is limited to Lender Edition clients under an executed API Agreement and NDA, keys and testing-site access are issued by the support desk, and there is no public developer portal or self-serve API reference. The API entries below are honestly modeled from the vendor-integration and marketplace capabilities LendingPad describes
  publicly; endpoint-level surfaces are not published and are not fabricated here.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lendingpad.png
layout: provider
modified: '2026-07-04'
name: LendingPad
nav: Providers
network: true
overview: 'LendingPad publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Mortgage, Loan Origination System, LOS, Lending, and FinTech.


  LendingPad''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Lendingpad Plans Pricing
  plan_count: 4
  slug: lendingpad-plans-pricing
random_paper: 26
score:
  band: emerging
  composite: 18.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Lendingpad Domain Security
  slug: lendingpad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Lendingpad Trust Center
  slug: lendingpad-trust-center
  summary_line: SOC 2
slug: lendingpad
tags:
- Mortgage
- Loan Origination System
- LOS
- Lending
- FinTech
- Financial Services
- Real Estate
- Partner API
- Gated API
website: https://lendingpad.com
---

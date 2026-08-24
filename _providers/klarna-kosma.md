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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.0
  scored_at: '2026-08-24'
api_count: 6
apis:
- description: The XS2A API is the server-side endpoint set used by TPPs and merchants to create and control Open Banking sessions and flows under PSD2. The XS2A API drives Account Information Services (AIS) for ret
  name: Klarna Kosma XS2A API
  slug: klarna-kosma-xs2a-api
- description: The Auth API is the client-session companion to the XS2A API. Whenever the Open Banking flow requires consumer interaction (bank selection, strong customer authentication, multi-step form completion),
  name: Klarna Kosma Auth API
  slug: klarna-kosma-auth-api
- description: The Consent API exposes the PSD2 consent lifecycle so TPPs can list, inspect, refresh, and revoke the consents granted by Payment Service Users (PSU). PSD2 obliges Klarna Kosma and its clients to keep
  name: Klarna Kosma Consent API
  slug: klarna-kosma-consent-api
- description: Kosma Insights turns raw Open Banking transaction data into categorised spend, income, and affordability signals. Insights covers 200+ spend categories and surfaces income streams, recurring outflows,
  name: Klarna Kosma Insights API
  slug: klarna-kosma-insights-api
- description: Kosma KYC layers account ownership and identity verification on top of the Kosma AIS connectivity. It confirms that the consumer authenticating against their bank is the legitimate account holder, ret
  name: Klarna Kosma KYC API
  slug: klarna-kosma-kyc-api
- description: 'Kosma Payments is the white-labeled PSD2 Payment Initiation Service (PIS) product. It lets merchants and platforms trigger account-to-account bank transfers directly from a consumer''s bank, bypassing '
  name: Klarna Kosma Payments API
  slug: klarna-kosma-payments-api
artifact_total: 23
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/klarna-kosma-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/klarna-kosma-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.klarna.com/kosma/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openbanking.klarna.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.openbanking.klarna.com/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openbanking.klarna.com/xs2a/urls.html
- group: auth
  title: ''
  type: Authentication
  url: https://docs.openbanking.klarna.com/xs2a/authentication.html
- group: start
  title: ''
  type: Sandbox
  url: https://docs.openbanking.klarna.com/xs2a/test-bank-psd2.html
- group: start
  title: ''
  type: Sandbox
  url: https://docs.openbanking.klarna.com/xs2a/test-banks.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openbanking.klarna.com/xs2a/onboarding_aspsps.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openbanking.klarna.com/xs2a/branded-go-live.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openbanking.klarna.com/xs2a/components.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openbanking.klarna.com/xs2a/xs2a-app.html
- group: build
  title: ''
  type: CodeExamples
  url: https://docs.openbanking.klarna.com/xs2a/xs2a-form/examples.html
- group: operate
  title: ''
  type: PressRelease
  url: https://www.klarna.com/international/press/klarna-launches-klarna-kosma-sub-brand-and-business-unit-to-harness-rapid-growth-of-open-banking-platform/
- group: operate
  title: ''
  type: PressRelease
  url: https://www.klarna.com/international/press/klarna-launches-open-banking-platform/
- group: operate
  title: ''
  type: PressRelease
  url: https://www.klarna.com/international/press/
- group: docs
  title: ''
  type: Documentation
  url: https://www.openbanking.org.uk/regulated-providers/klarna-kosma/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/klarna-kosma/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/klarna
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.klarna.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.klarna.com/international/privacy-notice/
- group: operate
  title: ''
  type: Support
  url: https://www.klarna.com/kosma/
created: '2026-05-25T00:00:00.000Z'
description: Klarna Kosma is the Open Banking platform spun out of Klarna in March 2022 as a dedicated sub-brand and business unit. Built on the connectivity infrastructure Klarna originally created for SOFORT, Kosma offers a single PSD2 XS2A API that aggregates more than 15,000 banks across 27 European and UK markets with >95% per-market coverage. The platform exposes Account Information Services (AIS) and Payment Initiation Services (PIS) plus higher-level products — Kosma Insights (categorised transaction, income, and affordability data across 200+ categories), Kosma KYC (account ownership and identity verification), and Kosma Payments (white-labeled account-to-account bank transfers). Kosma serves banks, lenders, fintechs, merchants, SMEs, and freelancers, and also powers Klarna's own BNPL underwriting and SOFORT bank-transfer rails. The XS2A API is paired with an embeddable XS2A App / JS widget that handles consumer bank selection and Strong Customer Authentication (SCA), and a Consent
  API that exposes the full PSD2 consent lifecycle.
features:
- PSD2-licensed Account Information Service (AIS) across the EEA and UK
- PSD2-licensed Payment Initiation Service (PIS) for account-to-account bank transfers
- Single XS2A API aggregating 15,000+ banks across 27 countries with >95% per-market coverage
- XS2A App — embeddable iframe/JavaScript widget for consumer bank selection and SCA
- Auth API for client-session-scoped consumer interactions and form submission
- Consent API for PSD2 consent lifecycle management (grant, refresh, revoke)
- Kosma Insights — transaction categorisation across 200+ categories with income and affordability signals
- Kosma KYC — account ownership and identity verification on top of AIS connectivity
- Kosma Payments — white-labeled PSD2 PIS for merchant checkout and platform payouts
- PSD2 test bank with embedded, decoupled, and redirect SCA methods
- Sandbox (api.openbanking.playground.klarna.com) and production environments
- Strong Customer Authentication (SCA) orchestration handled end-to-end by Kosma
- Underpins Klarna BNPL underwriting and SOFORT bank-transfer rails internally
- Pan-European regulatory coverage via Klarna Bank AB (publ) licensing
- Spun out as Klarna Kosma sub-brand and dedicated business unit in March 2022
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/klarna-kosma.png
layout: provider
modified: '2026-05-25'
name: Klarna Kosma
nav: Providers
network: true
overview: 'Klarna Kosma publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Open Banking, PSD2, AIS, PIS, and Account Information.


  Klarna Kosma''s developer surface includes developer portal, documentation, getting-started guide, authentication, sandbox, code examples, support, and 16 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 23.9
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 1.4
    developer_ergonomics: 54.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 23.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 32.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Klarna Kosma Domain Security
  slug: klarna-kosma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Klarna Kosma Vulnerability Disclosure
  slug: klarna-kosma-vulnerability-disclosure
  summary_line: Hackerone
slug: klarna-kosma
tags:
- Open Banking
- PSD2
- AIS
- PIS
- Account Information
- Payment Initiation
- KYC
- Identity Verification
- Categorization
- Insights
- Embedded Finance
- BNPL
- Lending
- Fintech
- Banking
website: https://www.klarna.com/kosma/
---

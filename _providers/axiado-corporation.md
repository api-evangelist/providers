---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The SecureStack Application Development Kit is Axiado's public API for building secure applications on the AX3000 / AX2000 TCU family. It exposes thread-safe engine interfaces for crypto (AES, SHA/SHA
  name: Axiado SecureStack ADK
  slug: axiado-securestack-adk
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/axiado-corporation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://axiado.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://devhub.axiado.com/
- group: docs
  title: ''
  type: Documentation
  url: https://devhub.axiado.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://devhub.axiado.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://devhub.axiado.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://devhub.axiado.com/discuss
- group: operate
  title: ''
  type: HelpCenter
  url: https://axiado-external.atlassian.net/
- group: start
  title: ''
  type: Login
  url: https://devhub.axiado.com/login
- group: company
  title: ''
  type: Blog
  url: https://axiado.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://axiado.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/axiado
- group: commercial
  title: ''
  type: TermsOfService
  url: https://axiado.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://axiado.com/privacy/
- group: operate
  title: ''
  type: ContactUs
  url: https://axiado.com/contact/
- group: other
  title: ''
  type: Products
  url: https://axiado.com/products/
- group: other
  title: ''
  type: Technology
  url: https://axiado.com/tcu-platform/
- group: company
  title: ''
  type: Careers
  url: https://axiado.com/joinus/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/axiado-corporation
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/axiado
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/axiado-corporation_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/axiado-corporation-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/axiado-corporation-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/axiado-corporation-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/axiado-corporation-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/axiado-corporation-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/axiado-corporation-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/axiado-corporation-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/axiado-corporation-authentication.yml
created: '2026-07-31'
description: Axiado Corporation is a San Jose, California semiconductor company building hardware-anchored, AI-driven platform security for AI data centers, cloud infrastructure, 5G networks and disaggregated compute. Its flagship Trusted Control/Compute Unit (TCU) — the AX3000 family and the second-generation AX3080 — collapses the baseboard management controller (BMC), hardware root of trust, trusted platform module (TPM), hardware security module, firewall and LAN-on-motherboard into a single system-on-chip with on-die AI/ML engines for dynamic threat management. Axiado ships OCP DC-SCM secure control modules (Smart-SCM3002, SCM3003, SCM3080-MT) alongside the SecureStack ADK, a Zephyr RTOS software development kit whose public API reference documents crypto, key management, X.509 certificate, BMC control, flash, SPI, DMA and OS-abstraction engines, plus OpenBMC-based out-of-band management running on the TCU. Developer documentation is published at devhub.axiado.com. The API surface is
  an embedded C/C++ SDK and on-device management interface — Axiado publishes no hosted public web API and no OpenAPI definition.
image: https://axiado.com/wp-content/uploads/2024/07/AXIADO_HORIZONTAL_PRIMARY.png
layout: provider
modified: '2026-07-31'
name: Axiado Corporation
nav: Providers
network: true
overview: 'Axiado Corporation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Semiconductors, Hardware Security, Platform Security, Data-Center, and Cybersecurity.


  Axiado Corporation''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 23 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 11
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 23.8
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/axiado-corporation/refs/heads/main/screenshots/axiado-corporation-2026-08-07T162032.png
security:
- kind: authentication
  name: Axiado Corporation Authentication
  slug: axiado-corporation-authentication
  summary_line: application-privilege/code-signing · 3 schemes
- kind: domain-security
  name: Axiado Corporation Domain Security
  slug: axiado-corporation-domain-security
  summary_line: TLSv1.3 · HSTS
slug: axiado-corporation
tags:
- Semiconductors
- Hardware Security
- Platform Security
- Data-Center
- Cybersecurity
- Baseboard Management Controller
- Root of Trust
- Firmware
- Embedded
- Cryptography
- AI Infrastructure
- Trusted Computing
- OpenBMC
- SDK
website: https://axiado.com/
---

---
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
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-17'
api_count: 2
apis:
- description: The HTTP API behind the Anitian SecureCloud and FedFlex console at securecloud.anitian.com. Anitian documents (in its FedRAMP 20x pilot README) that "an API is available for auditors to download evide
  name: Anitian SecureCloud / FedFlex Platform API
  slug: securecloud-platform
- description: 'An AWS API Gateway WebSocket API fronting the FedFlex agentic-AI copilot. Every plain HTTP request to copilot.anitian.com returns HTTP 426 Upgrade Required with a Sec-WebSocket-Version: 13 header; a W'
  name: Anitian FedFlex Copilot WebSocket API
  slug: fedflex-copilot
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anitian-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.anitian.com/
- group: company
  title: ''
  type: About
  url: https://www.anitian.com/about/
- group: company
  title: ''
  type: Blog
  url: https://www.anitian.com/all-posts/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.anitian.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.anitian.com/contact/
- group: start
  title: ''
  type: SignUp
  url: https://securecloud.anitian.com/auth/signin
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/marketplace/seller-profile?id=31e28297-b7d4-416f-b454-59f1d0aa8865
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anitian.com/marketplace-eula/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anitian.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anitianinc
- group: company
  title: ''
  type: Partners
  url: https://www.anitian.com/partner-program/
- group: other
  title: ''
  type: CaseStudies
  url: https://www.anitian.com/resources/case-studies/
- group: design
  title: ''
  type: Conformance
  url: conformance/anitian-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/anitian-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/anitian-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anitian-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Anitian's own FedRAMP 20x README says an API exists for auditors to download evidence, but the SecureCloud/FedFlex console at securecloud.anitian.com answers HTTP 307 to /auth/signin for every path including /openapi.json and /api-docs — only /api/health and the NextAuth /api/auth/* endpoints respond anonymously — and the FedFlex copilot API at copilot.anitian.com is a WebSocket-only AWS API Gateway whose $connect route returns 401, so no contract is reachable without a tenant or auditor account.
  evidence:
  - status: 307
    url: https://securecloud.anitian.com/openapi.json
  - status: 307
    url: https://securecloud.anitian.com/api-docs
  - status: 200
    url: https://securecloud.anitian.com/api/health
  - status: 426
    url: https://copilot.anitian.com/
  - status: 404
    url: https://www.anitian.com/openapi.json
  reason: customer-only-docs
  state: gated
created: '2026-08-06'
description: Anitian, Inc. is a Portland, Oregon cloud security and compliance automation company that helps SaaS providers reach and maintain U.S. federal compliance. Its FedFlex platform automates the FedRAMP lifecycle — pre-engineered AWS and Azure landing zones, AI-driven evidence collection mapped to FedRAMP 20x Key Security Indicators (KSIs) and NIST 800-53 controls, SSP generation, an auditor view for 3PAOs, and continuous monitoring — sold as FedFlex Starter (FedRAMP Low via the sponsorless 20x pilot) and FedFlex Comprehensive (Moderate/High). Anitian also sells SecureCloud compliance automation for ISO 27001, CMMC and commercial frameworks, plus managed SecOps. The company published a machine-readable FedRAMP 20x Phase One pilot package — a KSI-aligned assessment file, its data schema, and a signed 3PAO attestation from A-LIGN — publicly on GitHub. Anitian merged with Arkenstone Defense in April 2026 and now operates as "Anitian, powered by Arkenstone".
image: https://www.anitian.com/wp-content/uploads/2023/08/Anitian-blue-logo.svg
layout: provider
modified: '2026-08-06'
name: Anitian
nav: Providers
network: true
overview: 'Anitian publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Compliance, Cloud, and Governance.


  Anitian''s developer surface includes engineering blog, support, signup flow, pricing, authentication, and 12 more developer resources.'
random_paper: 144
score:
  band: thin
  composite: 28.6
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 28.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 55.6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anitian/refs/heads/main/screenshots/anitian-2026-08-07T161415.png
security:
- kind: authentication
  name: Anitian Authentication
  slug: anitian-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Anitian Domain Security
  slug: anitian-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anitian
tags:
- Company
- Security
- Compliance
- Cloud
- Governance
- FedRAMP
- Government
- Risk
- Audit
- Automation
website: https://www.anitian.com/
---

---
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: An unauthenticated, read-only JSON endpoint published on Immunefi's own domain that returns the complete catalog of bug bounty programs listed on the platform. Each record carries the project name and
  name: Immunefi Bug Bounty Programs API
  slug: bounties
artifact_total: 8
asyncapis:
- description: ''
  name: Immunefi Webhooks
  slug: immunefi-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://immunefi.com/
- group: company
  title: ''
  type: Blog
  url: https://immunefi.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://immunefi.com/blog/feed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/immunefi-team
- group: operate
  title: ''
  type: Support
  url: https://immunefisupport.zendesk.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://immunefi.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://immunefi.com/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://bugs.immunefi.com/
- group: auth
  title: ''
  type: Security
  url: https://immunefi.com/bug-bounty/immunefi/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/immunefi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/immunefi-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/immunefi-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/immunefi-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/immunefi-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/immunefi-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/immunefi-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/immunefi-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/immunefi-llms.txt
created: '2026-08-23'
description: Immunefi is a crowdsourced web3 security platform that operates the largest onchain bug bounty ecosystem, connecting security researchers with blockchain protocols and rewarding them for responsibly disclosed vulnerabilities. Alongside bug bounties it runs audit competitions and attackathons, PR reviews, Safe Harbor agreements, onchain monitoring, and Magnus, a unified security command center. Immunefi authors and versions the Immunefi Vulnerability Severity Classification System, the severity taxonomy most web3 bounty programs are written against. Its only public machine-readable surface is an unauthenticated JSON endpoint at immunefi.com/public-api/bounties.json that returns the full catalog of live bug bounty programs, including assets in scope, reward tables by severity, impacts, ecosystems and program metadata.
examples:
- key_count: 59
  name: Immunefi Bounty Program Example
  slug: immunefi-bounty-program-example
image: https://images.ctfassets.net/t3wqy70tc3bv/1XjTFUMSo1pLNrTF0aIH4U/353cf547e2cd9dcfc4e464ce9c328c07/Logo_square.png
layout: provider
modified: '2026-08-23'
name: Immunefi
nav: Providers
network: true
overview: 'Immunefi publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Bug Bounty, Vulnerability Disclosure, and Web3.


  The Immunefi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Immunefi''s developer surface includes engineering blog, support, signup flow, and 15 more developer resources.'
plans:
- name: Immunefi Plans Pricing
  plan_count: 0
  slug: immunefi-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Immunefi Rate Limits
  slug: immunefi-rate-limits
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 49.3
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 21.1
  previous_composite: 33.1
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Immunefi Authentication
  slug: immunefi-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Immunefi Domain Security
  slug: immunefi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Immunefi Vulnerability Disclosure
  slug: immunefi-vulnerability-disclosure
  summary_line: disclosure policy published
slug: immunefi
tags:
- Company
- Security
- Bug Bounty
- Vulnerability Disclosure
- Web3
- Blockchain
- Smart Contracts
- Application Security
- Cryptocurrency
- Crowdsourced Security
website: https://immunefi.com/
---

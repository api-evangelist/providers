---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Gandi Agentic Access
  operation_count: 37
  slug: gandi-agentic-access
  summary_line: 37 operations · 19 acting · 1 human-in-the-loop
api_count: 17
apis:
- description: The Gandi Certificate API allows you to manage SSL/TLS certificates.
  name: Gandi Certificate API
  slug: certificate
- description: The Gandi Email API allows you to manage email accounts and mailboxes.
  name: Gandi Email API
  slug: email
- description: The Gandi Billing API allows you to manage account billing information.
  name: Gandi Billing API
  slug: billing
- description: The Gandi Organization API allows you to manage organizations and users.
  name: Gandi Organization API
  slug: organization
- description: The Gandi Web Hosting API allows you to manage Simple Hosting instances.
  name: Gandi Web Hosting API
  slug: simplehosting
- description: The GandiCloud VPS API allows you to manage virtual private servers.
  name: Gandi Cloud VPS API
  slug: gandicloud
- description: Manage domain authorization codes.
  name: Gandi Authorization API
  slug: gandi-authorization-api
- description: Check domain name availability and pricing.
  name: Gandi Availability API
  slug: gandi-availability-api
- description: Manage DNSSEC keys for a domain.
  name: Gandi DNSSEC API
  slug: gandi-dnssec-api
- description: Manage domains.
  name: Gandi Domains API
  slug: gandi-domains-api
- description: Domain ownership changes.
  name: Gandi Ownership API
  slug: gandi-ownership-api
- description: Manage DNS records for a domain.
  name: Gandi Records API
  slug: gandi-records-api
- description: Manage automatic renewal.
  name: Gandi Renewal API
  slug: gandi-renewal-api
- description: Trademark claim information.
  name: Gandi Trademark API
  slug: gandi-trademark-api
- description: Manage TSIG keys for zone transfers.
  name: Gandi TSIG API
  slug: gandi-tsig-api
- description: Utility endpoints for record types.
  name: Gandi Utilities API
  slug: gandi-utilities-api
- description: Manage AXFR zone transfer settings.
  name: Gandi Zone Transfers API
  slug: gandi-zone-transfers-api
artifact_total: 37
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gandi Domain Authorization API
  slug: open-gandi-authorization-api
- collection_type: open
  name: Gandi Domain Authorization Availability API
  slug: open-gandi-availability-api
- collection_type: open
  name: Gandi Domain Authorization DNSSEC API
  slug: open-gandi-dnssec-api
- collection_type: open
  name: Gandi Domain Authorization Domains API
  slug: open-gandi-domains-api
- collection_type: open
  name: Gandi Domain Authorization Ownership API
  slug: open-gandi-ownership-api
- collection_type: open
  name: Gandi Domain Authorization Records API
  slug: open-gandi-records-api
- collection_type: open
  name: Gandi Domain Authorization Renewal API
  slug: open-gandi-renewal-api
- collection_type: open
  name: Gandi Domain Authorization Trademark API
  slug: open-gandi-trademark-api
- collection_type: open
  name: Gandi Domain Authorization TSIG API
  slug: open-gandi-tsig-api
- collection_type: open
  name: Gandi Domain Authorization Utilities API
  slug: open-gandi-utilities-api
- collection_type: open
  name: Gandi Domain Authorization Zone Transfers API
  slug: open-gandi-zone-transfers-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gandi-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gandi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gandi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gandi-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Gandi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gandi
- group: company
  title: ''
  type: Website
  url: https://www.gandi.net/
- group: docs
  title: ''
  type: Documentation
  url: https://api.gandi.net/docs/reference/
- group: start
  title: ''
  type: Sandbox
  url: https://api.sandbox.gandi.net/docs/
- group: company
  title: ''
  type: Blog
  url: https://news.gandi.net/en/feed
created: '2025-02-09'
description: Gandi is a domain name registrar and web hosting provider. The Gandi v5 Public API exposes domain management, LiveDNS, certificates, email, organization, billing, and hosting capabilities for programmatic use.
finops:
- name: Gandi Finops
  service_category: Domain Registrar & DNS
  slug: gandi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gandi.png
json_structures:
- name: Gandi Structure
  property_count: 0
  slug: gandi-structure
layout: provider
modified: '2026-05-19'
name: Gandi
nav: Providers
network: true
overview: 'Gandi publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Availability API, DNSSEC API, and 8 more. Tagged areas include DNS, Domains, Domain Registrar, Email, and Hosting.


  Gandi''s developer surface includes authentication, documentation, sandbox, engineering blog, and 6 more developer resources.'
plans:
- name: Gandi Plans Pricing
  plan_count: 2
  slug: gandi-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Gandi Rate Limits
  slug: gandi-rate-limits
score:
  band: thin
  composite: 31.0
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 55.2
    developer_ergonomics: 31.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 31.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 33.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gandi/refs/heads/main/screenshots/gandi-2026-06-20T181644.png
security:
- kind: authentication
  name: Gandi Authentication
  slug: gandi-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Gandi Domain Security
  slug: gandi-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gandi Vulnerability Disclosure
  slug: gandi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: gandi
tags:
- DNS
- Domains
- Domain Registrar
- Email
- Hosting
- Certificates
website: https://www.gandi.net/
---

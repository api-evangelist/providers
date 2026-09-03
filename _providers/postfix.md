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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 0.0
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Postfix implements SMTP (RFC 5321) for sending and receiving electronic mail, with submission (port 587), SMTPS (port 465), and standard SMTP (port 25) endpoints. There is no public HTTP/REST API; int
  name: Postfix SMTP
  slug: smtp
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/postfix-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postfix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.postfix.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.postfix.org/documentation.html
- group: other
  title: ''
  type: Download
  url: https://www.postfix.org/download.html
- group: build
  title: ''
  type: Source Code
  url: https://github.com/vdukhovni/postfix
- group: other
  title: ''
  type: Mailing Lists
  url: https://www.postfix.org/lists.html
- group: auth
  title: ''
  type: Security
  url: https://www.postfix.org/security.html
- group: commercial
  title: ''
  type: License
  url: https://www.postfix.org/license.html
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Postfix_(software)
created: '2026-05-11'
description: Postfix is a free, open source mail transfer agent (MTA) originally written by Wietse Venema at IBM Research as a fast, secure, and easy-to-administer alternative to Sendmail. It runs on UNIX-like systems including Linux, BSD, and macOS, routing and delivering email over SMTP with extensive support for TLS, SASL, DKIM/SPF/DMARC integration, content filtering, and policy delegation. Postfix is administered via configuration files (main.cf, master.cf) and command-line tools rather than a public HTTP API, and is one of the most widely deployed mail servers on the internet.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/postfix.png
layout: provider
modified: '2026-05-11'
name: Postfix
nav: Providers
network: true
overview: 'Postfix publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Email, Mail Server, MTA, SMTP, and Open-Source.


  Postfix''s developer surface includes documentation and 9 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 2
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 9.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/postfix/refs/heads/main/screenshots/postfix-2026-06-20T191954.png
security:
- kind: domain-security
  name: Postfix Domain Security
  slug: postfix-domain-security
  summary_line: TLSv1.3 · DNSSEC
- kind: vulnerability-disclosure
  name: Postfix Vulnerability Disclosure
  slug: postfix-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: postfix
tags:
- Email
- Mail Server
- MTA
- SMTP
- Open-Source
- Infrastructure
website: https://www.postfix.org
---

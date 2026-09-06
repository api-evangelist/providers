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
  band: human-only
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
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: HTTP-based Remote API served from Webmin's remote.cgi on port 10000. Each call passes a `program` parameter naming one of ~200 command-line programs (create-domain, list-domains, create-user, create-a
  name: Virtualmin Remote API
  slug: virtualmin-remote-api
artifact_total: 3
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.virtualmin.com/docs/development/
- group: docs
  title: ''
  type: Documentation
  url: https://www.virtualmin.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.virtualmin.com/docs/development/remote-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.virtualmin.com/docs/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://www.virtualmin.com/support/
- group: operate
  title: ''
  type: Community
  url: https://forum.virtualmin.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/virtualmin
- group: other
  title: ''
  type: Download
  url: https://www.virtualmin.com/download/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.virtualmin.com/shop/
- group: start
  title: ''
  type: Login
  url: https://www.virtualmin.com/account/signin/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.virtualmin.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.virtualmin.com/privacy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/virtualmin-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/virtualmin-conventions.yml
- group: build
  title: ''
  type: CLI
  url: cli/virtualmin-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/virtualmin-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/virtualmin-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/virtualmin-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/virtualmin-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/virtualmin-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/virtualmin-domain-security.yml
created: '2026-07-17'
description: Virtualmin is an open-source web hosting control panel for Linux and BSD, built on top of Webmin, that lets administrators and resellers manage websites, virtual servers, DNS, email, FTP, databases, SSL certificates, WordPress and more from a single interface. Distributed as a community GPL edition and a commercial Pro edition, Virtualmin (with its sibling Cloudmin for VM/cloud management) has run for 20+ years and manages over a million domains across 200K+ active users. For automation it exposes a command-line API and an HTTP-based Remote API served from Webmin's remote.cgi on port 10000, covering ~200 documented programs for creating and modifying virtual servers, users, aliases, databases, resellers, plans, templates, SSL certs, backups and cloud storage, with plain-text, JSON, XML or Perl output.
image: https://www.virtualmin.com/apple-touch-icon.png
layout: provider
modified: '2026-07-21'
name: Virtualmin
nav: Providers
network: true
overview: 'Virtualmin publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Web Hosting, Control Panel, Server Management, and Webmin.


  Virtualmin''s developer surface includes documentation, API reference, getting-started guide, support, pricing, authentication, CLI, and 14 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 27.9
  provenance:
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/virtualmin/refs/heads/main/screenshots/virtualmin-2026-09-02T170019.png
security:
- kind: authentication
  name: Virtualmin Authentication
  slug: virtualmin-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Virtualmin Domain Security
  slug: virtualmin-domain-security
  summary_line: TLSv1.3
slug: virtualmin
tags:
- Company
- Web Hosting
- Control Panel
- Server Management
- Webmin
- DNS
- Email
- Domains
- Virtual Servers
- Databases
- SSL
- WordPress
- Open-Source
- Linux
website: https://www.virtualmin.com/docs/development/
---

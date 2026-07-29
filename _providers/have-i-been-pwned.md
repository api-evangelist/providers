---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Have I Been Pwned Agentic Access
  operation_count: 17
  slug: have-i-been-pwned-agentic-access
  summary_line: 17 operations · 3 acting
api_count: 16
apis:
- description: REST API for searching breached accounts, pastes, breach metadata, domain breach data, and stealer log entries. Authentication requires an hibp-api-key header (32-character key) along with a descripti
  name: Have I Been Pwned API v3
  slug: api-v3
- description: Free, unauthenticated, k-anonymity-based API to check whether a password hash appears in the 800+ million record Pwned Passwords dataset. Clients submit the first five characters of a SHA-1 hash and r
  name: Pwned Passwords API
  slug: pwned-passwords
- description: The Breach API from Have I Been Pwned — 1 operation(s) for breach.
  name: Have I Been Pwned Breach API
  slug: have-i-been-pwned-breach-api
- description: The Breachedaccount API from Have I Been Pwned — 2 operation(s) for breachedaccount.
  name: Have I Been Pwned Breachedaccount API
  slug: have-i-been-pwned-breachedaccount-api
- description: The Breacheddomain API from Have I Been Pwned — 1 operation(s) for breacheddomain.
  name: Have I Been Pwned Breacheddomain API
  slug: have-i-been-pwned-breacheddomain-api
- description: The Breaches API from Have I Been Pwned — 1 operation(s) for breaches.
  name: Have I Been Pwned Breaches API
  slug: have-i-been-pwned-breaches-api
- description: The Dataclasses API from Have I Been Pwned — 1 operation(s) for dataclasses.
  name: Have I Been Pwned Dataclasses API
  slug: have-i-been-pwned-dataclasses-api
- description: The Domainverification API from Have I Been Pwned — 3 operation(s) for domainverification.
  name: Have I Been Pwned Domainverification API
  slug: have-i-been-pwned-domainverification-api
- description: The Latestbreach API from Have I Been Pwned — 1 operation(s) for latestbreach.
  name: Have I Been Pwned Latestbreach API
  slug: have-i-been-pwned-latestbreach-api
- description: The Pasteaccount API from Have I Been Pwned — 1 operation(s) for pasteaccount.
  name: Have I Been Pwned Pasteaccount API
  slug: have-i-been-pwned-pasteaccount-api
- description: The Range API from Have I Been Pwned — 1 operation(s) for range.
  name: Have I Been Pwned Range API
  slug: have-i-been-pwned-range-api
- description: The Stealerlogsbyemail API from Have I Been Pwned — 1 operation(s) for stealerlogsbyemail.
  name: Have I Been Pwned Stealerlogsbyemail API
  slug: have-i-been-pwned-stealerlogsbyemail-api
- description: The Stealerlogsbyemaildomain API from Have I Been Pwned — 1 operation(s) for stealerlogsbyemaildomain.
  name: Have I Been Pwned Stealerlogsbyemaildomain API
  slug: have-i-been-pwned-stealerlogsbyemaildomain-api
- description: The Stealerlogsbywebsitedomain API from Have I Been Pwned — 1 operation(s) for stealerlogsbywebsitedomain.
  name: Have I Been Pwned Stealerlogsbywebsitedomain API
  slug: have-i-been-pwned-stealerlogsbywebsitedomain-api
- description: The Subscribeddomains API from Have I Been Pwned — 1 operation(s) for subscribeddomains.
  name: Have I Been Pwned Subscribeddomains API
  slug: have-i-been-pwned-subscribeddomains-api
- description: The Subscription API from Have I Been Pwned — 1 operation(s) for subscription.
  name: Have I Been Pwned Subscription API
  slug: have-i-been-pwned-subscription-api
artifact_total: 21
collections:
- collection_type: open
  name: Have I Been Pwned API v3
  slug: open-have-i-been-pwned
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/have-i-been-pwned-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/have-i-been-pwned-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/have-i-been-pwned-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/have-i-been-pwned-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HaveIBeenPwned
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/haveibeenpwned
- group: company
  title: ''
  type: Website
  url: https://haveibeenpwned.com
- group: docs
  title: ''
  type: Documentation
  url: https://haveibeenpwned.com/API/v3
- group: commercial
  title: ''
  type: Pricing
  url: https://haveibeenpwned.com/API/Key
- group: start
  title: ''
  type: Signup
  url: https://haveibeenpwned.com/API/Key
- group: operate
  title: ''
  type: FAQ
  url: https://haveibeenpwned.com/FAQs
- group: company
  title: ''
  type: Blog
  url: https://www.troyhunt.com
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/haveibeenpwned
created: '2026-05-11'
description: Have I Been Pwned (HIBP) is a free service operated by Troy Hunt that lets individuals and organizations check whether their email addresses, phone numbers, passwords, or domains have appeared in known data breaches, pastes, or stealer logs. The service aggregates billions of compromised records and exposes both free and paid endpoints, including the k-anonymity Pwned Passwords API. The v3 REST API at haveibeenpwned.com requires an hibp-api-key header for breach, paste, domain, and stealer log endpoints and is offered across Core, Pro, and High RPM subscription tiers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/have-i-been-pwned.png
layout: provider
modified: '2026-05-11'
name: Have I Been Pwned
nav: Providers
network: true
overview: 'Have I Been Pwned publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Breach API, Breachedaccount API, Breacheddomain API, and 11 more. Tagged areas include Security, Data Breaches, Pwned Passwords, Identity, and Threat Intelligence.


  Have I Been Pwned''s developer surface includes authentication, documentation, pricing, signup flow, FAQ, engineering blog, and 7 more developer resources.'
random_paper: 32
score:
  band: thin
  composite: 28.1
  delta: -2.1
  facets:
    commercial_clarity: 10.5
    contract_quality: 54.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 30.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/have-i-been-pwned/refs/heads/main/screenshots/have-i-been-pwned-2026-06-20T182538.png
security:
- kind: authentication
  name: Have I Been Pwned Authentication
  slug: have-i-been-pwned-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Have I Been Pwned Domain Security
  slug: have-i-been-pwned-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Have I Been Pwned Vulnerability Disclosure
  slug: have-i-been-pwned-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: have-i-been-pwned
tags:
- Security
- Data Breaches
- Pwned Passwords
- Identity
- Threat Intelligence
- Credential Stuffing
website: https://haveibeenpwned.com
---

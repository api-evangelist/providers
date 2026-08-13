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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.3
  scored_at: '2026-08-12'
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
artifact_total: 85
collections:
- collection_type: postman
  name: Have I Been Pwned API v3 Breached Accounts API
  slug: postman-have-i-been-pwned-breached-accounts-api
- collection_type: postman
  name: Have I Been Pwned API v3 Breached Accounts Breaches API
  slug: postman-have-i-been-pwned-breaches-api
- collection_type: postman
  name: Have I Been Pwned API v3 Breached Accounts Data Classes API
  slug: postman-have-i-been-pwned-data-classes-api
- collection_type: postman
  name: Have I Been Pwned API v3 Breached Accounts Domain Search API
  slug: postman-have-i-been-pwned-domain-search-api
- collection_type: postman
  name: Have I Been Pwned API v3 Breached Accounts Pastes API
  slug: postman-have-i-been-pwned-pastes-api
- collection_type: postman
  name: Have I Been Pwned API v3 Breached Accounts Range Search API
  slug: postman-have-i-been-pwned-range-search-api
- collection_type: postman
  name: Have I Been Pwned API v3 Breached Accounts Stealer Logs API
  slug: postman-have-i-been-pwned-stealer-logs-api
- collection_type: postman
  name: Have I Been Pwned API v3 Breached Accounts Subscription API
  slug: postman-have-i-been-pwned-subscription-api
- collection_type: open
  name: Have I Been Pwned API v3
  slug: open-have-i-been-pwned
- collection_type: open
  name: Have I Been Pwned API v3
  slug: open-hibp
- collection_type: open
  name: Pwned Passwords API
  slug: open-pwned-passwords
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
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/haveibeenpwned/overview
- group: start
  title: ''
  type: Portal
  url: https://haveibeenpwned.com
- group: commercial
  title: ''
  type: Plans
  url: plans/have-i-been-pwned-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/have-i-been-pwned-rate-limits.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://haveibeenpwned.com/API/v3#License
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://haveibeenpwned.com/Privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.haveibeenpwned.com
- group: operate
  title: ''
  type: Support
  url: https://haveibeenpwned.com/Contact
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: design
  title: ''
  type: SpectralRules
  url: rules/hibp-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/have-i-been-pwned-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/have-i-been-pwned-vocabulary.yml
- group: build
  title: Email Address Extractor (CLI)
  type: Tools
  url: https://github.com/HaveIBeenPwned/EmailAddressExtractor
- group: other
  title: ''
  type: Branding
  url: https://github.com/HaveIBeenPwned/Branding
created: '2026-05-11'
description: Have I Been Pwned (HIBP) is a free service operated by Troy Hunt that lets individuals and organizations check whether their email addresses, phone numbers, passwords, or domains have appeared in known data breaches, pastes, or stealer logs. The service aggregates billions of compromised records and exposes both free and paid endpoints, including the k-anonymity Pwned Passwords API. The v3 REST API at haveibeenpwned.com requires an hibp-api-key header for breach, paste, domain, and stealer log endpoints and is offered across Core, Pro, and High RPM subscription tiers.
examples:
- key_count: 3
  name: Hibp Generate Dns Token Example
  slug: hibp-generate-dns-token-example
- key_count: 3
  name: Hibp Get Breach By Name Example
  slug: hibp-get-breach-by-name-example
- key_count: 3
  name: Hibp Get Breached Domain Example
  slug: hibp-get-breached-domain-example
- key_count: 3
  name: Hibp Get Breaches By Range Example
  slug: hibp-get-breaches-by-range-example
- key_count: 3
  name: Hibp Get Breaches For Account Example
  slug: hibp-get-breaches-for-account-example
- key_count: 3
  name: Hibp Get Latest Breach Example
  slug: hibp-get-latest-breach-example
- key_count: 3
  name: Hibp Get Pastes For Account Example
  slug: hibp-get-pastes-for-account-example
- key_count: 3
  name: Hibp Get Stealer Logs By Email Domain Example
  slug: hibp-get-stealer-logs-by-email-domain-example
- key_count: 3
  name: Hibp Get Stealer Logs By Email Example
  slug: hibp-get-stealer-logs-by-email-example
- key_count: 3
  name: Hibp Get Stealer Logs By Website Domain Example
  slug: hibp-get-stealer-logs-by-website-domain-example
- key_count: 3
  name: Hibp Get Subscription Status Example
  slug: hibp-get-subscription-status-example
- key_count: 3
  name: Hibp List Breaches Example
  slug: hibp-list-breaches-example
- key_count: 3
  name: Hibp List Data Classes Example
  slug: hibp-list-data-classes-example
- key_count: 3
  name: Hibp List Subscribed Domains Example
  slug: hibp-list-subscribed-domains-example
- key_count: 4
  name: Pwned Passwords Search Range Example
  slug: pwned-passwords-search-range-example
features:
- description: Lookup all breaches containing an email address.
  name: Email Breach Search
- description: Privacy-preserving breach lookup by SHA-1 prefix.
  name: K-Anonymity Email Search
- description: Discover paste-site dumps referencing an email.
  name: Paste Search
- description: Surface infostealer captures by email, website domain, or email domain.
  name: Stealer Log Lookup
- description: Subscribe to monitor owned domains via DNS or email verification.
  name: Domain Monitoring
- description: Inspect monitored domains and pending renewals.
  name: Subscribed Domains Inventory
- description: K-anonymity password compromise lookups with optional response padding.
  name: Pwned Passwords (Free)
- description: Inspect the calling key's tier, RPM, and feature flags.
  name: Subscription Tier Introspection
finops:
- name: Have I Been Pwned Finops
  service_category: ''
  slug: have-i-been-pwned-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/have-i-been-pwned.png
integrations:
- description: 1Password leverages Pwned Passwords to flag compromised credentials.
  name: 1Password Watchtower
- description: Firefox's breach-notification feature is powered by HIBP.
  name: Mozilla Firefox Monitor
- description: Identity providers use Pwned Passwords to enforce password policies.
  name: Okta / Auth0
- description: Cloudflare hosts and accelerates the Pwned Passwords k-anonymity API.
  name: Cloudflare
- description: Banned-password lists can incorporate Pwned Passwords data.
  name: Microsoft Entra (Azure AD)
json_schemas:
- name: Breach
  property_count: 19
  slug: hibp-breach
- name: BreachedAccountRangeEntry
  property_count: 2
  slug: hibp-breached-account-range-entry
- name: Paste
  property_count: 5
  slug: hibp-paste
- name: SubscribedDomain
  property_count: 5
  slug: hibp-subscribed-domain
- name: SubscriptionStatus
  property_count: 11
  slug: hibp-subscription-status
- name: PwnedPasswordsRangeResult
  property_count: 2
  slug: pwned-passwords-range-result
json_structures:
- name: Hibp Breach Structure
  property_count: 0
  slug: hibp-breach-structure
- name: Hibp Paste Structure
  property_count: 0
  slug: hibp-paste-structure
- name: Hibp Subscription Status Structure
  property_count: 0
  slug: hibp-subscription-status-structure
jsonld:
- class_count: 12
  name: Have I Been Pwned Context
  property_count: 22
  slug: have-i-been-pwned-context
layout: provider
modified: '2026-08-08'
name: Have I Been Pwned
nav: Providers
network: true
overview: 'Have I Been Pwned publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Breach API, Breachedaccount API, Breacheddomain API, and 11 more. Tagged areas include Security, Data Breaches, Pwned Passwords, Identity, and Threat Intelligence.


  The Have I Been Pwned catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Have I Been Pwned''s developer surface includes authentication, documentation, pricing, signup flow, FAQ, engineering blog, developer portal, and 20 more developer resources.'
plans:
- name: Have I Been Pwned Plans Pricing
  plan_count: 6
  slug: have-i-been-pwned-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 0
  name: Have I Been Pwned Rate Limits
  slug: have-i-been-pwned-rate-limits
rules:
- name: Have I Been Pwned API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: have-i-been-pwned-jsonschema-spectral-rules
- name: Have I Been Pwned API Rules
  rule_count: 12
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 7
  slug: hibp-rules
score:
  band: strong
  composite: 59.1
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 64.3
    developer_ergonomics: 39.1
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 59.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  schema_version: 0.11.0
  scored_at: '2026-08-12'
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
solutions:
- description: Entry tier ($3.95/mo) for hobbyists and small projects.
  name: Pwned 1
- description: Mid-volume tier with stealer-log access.
  name: Pwned 2
- description: High-volume tier for security vendors and MSSPs.
  name: Pwned 3
- description: Enterprise tier with auto subdomain verification.
  name: Pwned 4
- description: Top tier ($995/mo) for large identity-protection platforms.
  name: Pwned 5
- description: Always-free k-anonymity password lookup at api.pwnedpasswords.com.
  name: Pwned Passwords (Free)
tags:
- Security
- Data Breaches
- Pwned Passwords
- Identity
- Threat Intelligence
- Credential Stuffing
use_cases:
- description: Block sign-ups using credentials known to be in public breaches.
  name: Account Takeover Prevention
- description: Quickly enumerate breaches and pastes touching an affected user.
  name: Incident Response Triage
- description: Continuously detect when a domain's users appear in new breaches.
  name: Domain Risk Monitoring
- description: Reject candidate passwords already present in the Pwned Passwords corpus.
  name: Password Strength Enforcement
- description: Detect infostealer-captured credentials before adversaries weaponize them.
  name: Stealer Log Notification
website: https://haveibeenpwned.com
---

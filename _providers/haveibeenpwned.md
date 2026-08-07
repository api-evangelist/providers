---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Haveibeenpwned Agentic Access
  operation_count: 17
  slug: haveibeenpwned-agentic-access
  summary_line: 17 operations · 3 acting
api_count: 8
apis:
- description: Lookup breaches affecting an email address.
  name: HaveIBeenPwned Breached Accounts API
  slug: haveibeenpwned-breached-accounts-api
- description: Browse breach metadata in the HIBP corpus.
  name: HaveIBeenPwned Breaches API
  slug: haveibeenpwned-breaches-api
- description: Enumerate classes of data exposed across breaches.
  name: HaveIBeenPwned Data Classes API
  slug: haveibeenpwned-data-classes-api
- description: Verify and search domains you control.
  name: HaveIBeenPwned Domain Search API
  slug: haveibeenpwned-domain-search-api
- description: Lookup pastes referencing an email address.
  name: HaveIBeenPwned Pastes API
  slug: haveibeenpwned-pastes-api
- description: K-anonymity range search for password hashes.
  name: HaveIBeenPwned Range Search API
  slug: haveibeenpwned-range-search-api
- description: Search infostealer malware corpora by email or domain.
  name: HaveIBeenPwned Stealer Logs API
  slug: haveibeenpwned-stealer-logs-api
- description: Inspect the calling key's subscription state.
  name: HaveIBeenPwned Subscription API
  slug: haveibeenpwned-subscription-api
artifact_total: 76
collections:
- collection_type: postman
  name: Have I Been Pwned API v3 Breached Accounts API
  slug: postman-haveibeenpwned-breached-accounts-api
- collection_type: postman
  name: Have I Been Pwned API v3 Breached Accounts Breaches API
  slug: postman-haveibeenpwned-breaches-api
- collection_type: postman
  name: Have I Been Pwned API v3 Breached Accounts Data Classes API
  slug: postman-haveibeenpwned-data-classes-api
- collection_type: postman
  name: Have I Been Pwned API v3 Breached Accounts Domain Search API
  slug: postman-haveibeenpwned-domain-search-api
- collection_type: postman
  name: Have I Been Pwned API v3 Breached Accounts Pastes API
  slug: postman-haveibeenpwned-pastes-api
- collection_type: postman
  name: Have I Been Pwned API v3 Breached Accounts Range Search API
  slug: postman-haveibeenpwned-range-search-api
- collection_type: postman
  name: Have I Been Pwned API v3 Breached Accounts Stealer Logs API
  slug: postman-haveibeenpwned-stealer-logs-api
- collection_type: postman
  name: Have I Been Pwned API v3 Breached Accounts Subscription API
  slug: postman-haveibeenpwned-subscription-api
- collection_type: open
  name: Have I Been Pwned API v3
  slug: open-hibp
- collection_type: open
  name: Pwned Passwords API
  slug: open-pwned-passwords
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/haveibeenpwned/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/haveibeenpwned-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/haveibeenpwned-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/haveibeenpwned-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/haveibeenpwned-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://haveibeenpwned.com
- group: start
  title: ''
  type: Portal
  url: https://haveibeenpwned.com
- group: start
  title: ''
  type: Signup
  url: https://haveibeenpwned.com/API/Key
- group: commercial
  title: ''
  type: Pricing
  url: https://haveibeenpwned.com/API/Key
- group: commercial
  title: ''
  type: Plans
  url: plans/haveibeenpwned-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/haveibeenpwned-rate-limits.yml
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
- group: company
  title: ''
  type: Blog
  url: https://www.troyhunt.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HaveIBeenPwned
- group: operate
  title: ''
  type: Support
  url: https://haveibeenpwned.com/Contact
- group: operate
  title: ''
  type: FAQ
  url: https://haveibeenpwned.com/FAQs
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
  url: json-ld/haveibeenpwned-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/haveibeenpwned-vocabulary.yml
- group: build
  title: Email Address Extractor (CLI)
  type: Tools
  url: https://github.com/HaveIBeenPwned/EmailAddressExtractor
- group: build
  title: Pwned Passwords Downloader (CLI)
  type: Tools
  url: https://github.com/HaveIBeenPwned/PwnedPasswordsDownloader
- group: build
  title: Cloudflare Prometheus Exporter
  type: Tools
  url: https://github.com/HaveIBeenPwned/cloudflare-prometheus-exporter
- group: other
  title: ''
  type: Branding
  url: https://github.com/HaveIBeenPwned/Branding
created: '2026-05-28'
description: Have I Been Pwned (HIBP) is Troy Hunt's free breach-notification and credential-exposure service. The HIBP API v3 lets clients search for email addresses, pastes, stealer-log entries, and monitored domains across the world's largest aggregated breach corpus. A separate free k-anonymity password lookup is offered at api.pwnedpasswords.com.
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
- name: Haveibeenpwned Finops
  service_category: ''
  slug: haveibeenpwned-finops
image: https://haveibeenpwned.com/Content/Images/PwnedLogoLargeFollowed.png
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
  name: Haveibeenpwned Context
  property_count: 22
  slug: haveibeenpwned-context
layout: provider
modified: '2026-05-30'
name: HaveIBeenPwned
nav: Providers
network: true
overview: 'HaveIBeenPwned publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Breached Accounts API, Breaches API, Data Classes API, and 5 more. Tagged areas include Security, Breach Notification, Credential Stuffing, Stealer Logs, and K-Anonymity.


  The HaveIBeenPwned catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  HaveIBeenPwned''s developer surface includes authentication, developer portal, signup flow, pricing, engineering blog, support, FAQ, and 19 more developer resources.'
plans:
- name: Haveibeenpwned Plans Pricing
  plan_count: 6
  slug: haveibeenpwned-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Haveibeenpwned Rate Limits
  slug: haveibeenpwned-rate-limits
rules:
- name: HaveIBeenPwned API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: haveibeenpwned-jsonschema-spectral-rules
- name: HaveIBeenPwned API Rules
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
    commercial_clarity: 71.1
    contract_quality: 78.7
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 59.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/haveibeenpwned/refs/heads/main/screenshots/haveibeenpwned-2026-06-20T182538.png
security:
- kind: authentication
  name: Haveibeenpwned Authentication
  slug: haveibeenpwned-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Haveibeenpwned Domain Security
  slug: haveibeenpwned-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Haveibeenpwned Vulnerability Disclosure
  slug: haveibeenpwned-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: haveibeenpwned
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
- Breach Notification
- Credential Stuffing
- Stealer Logs
- K-Anonymity
- Privacy
- Identity
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

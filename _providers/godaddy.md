---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 67
  human_in_the_loop: 2
  name: Godaddy Agentic Access
  operation_count: 119
  slug: godaddy-agentic-access
  summary_line: 119 operations · 67 acting · 2 human-in-the-loop
api_count: 10
apis:
- baseURL: https://api.godaddy.com
  baseurl_source: declared
  description: The Actions API from GoDaddy — 2 operation(s) for actions.
  name: GoDaddy Actions API
  slug: godaddy-actions-api
- baseURL: https://api.godaddy.com
  baseurl_source: declared
  description: The Contacts API from GoDaddy — 1 operation(s) for contacts.
  name: GoDaddy Contacts API
  slug: godaddy-contacts-api
- baseURL: https://api.godaddy.com
  baseurl_source: declared
  description: The Domains API from GoDaddy — 24 operation(s) for domains.
  name: GoDaddy Domains API
  slug: godaddy-domains-api
- baseURL: https://api.godaddy.com
  baseurl_source: declared
  description: API for auction-related actions exclusive to whitelisted partners.
  name: 'GoDaddy Expiry Auctions: Registrar Partners API'
  slug: godaddy-expiry-auctions-registrar-partners-api
- baseURL: https://api.godaddy.com
  baseurl_source: declared
  description: The Notifications API from GoDaddy — 4 operation(s) for notifications.
  name: GoDaddy Notifications API
  slug: godaddy-notifications-api
- baseURL: https://api.godaddy.com
  baseurl_source: declared
  description: The Abuse API from GoDaddy — 4 operation(s) for abuse.
  name: GoDaddy Abuse API
  slug: godaddy-abuse-api
- baseURL: https://api.godaddy.com
  baseurl_source: declared
  description: The Agreements API from GoDaddy — 1 operation(s) for agreements.
  name: GoDaddy Agreements API
  slug: godaddy-agreements-api
- baseURL: https://api.godaddy.com
  baseurl_source: declared
  description: The Certificates API from GoDaddy — 21 operation(s) for certificates.
  name: GoDaddy Certificates API
  slug: godaddy-certificates-api
- baseURL: https://api.godaddy.com
  baseurl_source: declared
  description: The Countries API from GoDaddy — 2 operation(s) for countries.
  name: GoDaddy Countries API
  slug: godaddy-countries-api
- baseURL: https://api.godaddy.com
  baseurl_source: declared
  description: The Customers API from GoDaddy — 5 operation(s) for customers.
  name: GoDaddy Customers API
  slug: godaddy-customers-api
- baseURL: https://api.godaddy.com
  baseurl_source: declared
  description: The Orders API from GoDaddy — 2 operation(s) for orders.
  name: GoDaddy Orders API
  slug: godaddy-orders-api
- baseURL: https://api.godaddy.com
  baseurl_source: declared
  description: The Shoppers API from GoDaddy — 4 operation(s) for shoppers.
  name: GoDaddy Shoppers API
  slug: godaddy-shoppers-api
- baseURL: https://api.godaddy.com
  baseurl_source: declared
  description: The Subscriptions API from GoDaddy — 3 operation(s) for subscriptions.
  name: GoDaddy Subscriptions API
  slug: godaddy-subscriptions-api
- baseURL: https://api.godaddy.com
  baseurl_source: declared
  description: Indicative, non-committing operations for finding and checking domains. Use suggestDomains for natural-language queries and getDomainAvailability for specific domain verification. Both return indicati
  name: GoDaddy Discovery API
  slug: godaddy-discovery-api
- baseURL: https://api.godaddy.com
  baseurl_source: declared
  description: 'Non-commercial async mutations on owned domain instances: contacts, nameservers, privacy, auto-renew, and transfer-lock. All sub-resources of /domain-names/{domain-name}. All mutations return a Domain'
  name: GoDaddy Domain Management API
  slug: godaddy-domain-management-api
- baseURL: https://api.godaddy.com
  baseurl_source: declared
  description: Abstract operation polling. Poll GET /operations/{operationId} for any domain mutation until it reaches COMPLETED or FAILED. Operation IDs are unique across Registration, Renewal, and Transfer — clien
  name: GoDaddy Operations API
  slug: godaddy-operations-api
- baseURL: https://api.godaddy.com
  baseurl_source: declared
  description: CRUD operations on DNS records within the GoDaddy-managed zone. Sub-collection of /zones/{zone}. Changes are applied synchronously.
  name: GoDaddy Records API
  slug: godaddy-records-api
- baseURL: https://api.godaddy.com
  baseurl_source: declared
  description: Quote a domain registration. Returns a locked price, resolved settings, required agreements, and a single-use quoteToken. Free and read-only.
  name: GoDaddy Registration Quotes API
  slug: godaddy-registration-quotes-api
- baseURL: https://api.godaddy.com
  baseurl_source: declared
  description: Top-level registration entity collection. Execute a domain registration by POSTing with a quoteToken, domain, period, and consent. Returns a Registration entity with links to the concrete poll URL (GE
  name: GoDaddy Registrations API
  slug: godaddy-registrations-api
artifact_total: 42
collections:
- collection_type: open
  name: Abuse API
  slug: open-godaddy-abuse
- collection_type: open
  name: Abuse Actions API
  slug: open-godaddy-actions-api
- collection_type: open
  name: Aftermarket API
  slug: open-godaddy-aftermarket
- collection_type: open
  name: API Collection
  slug: open-godaddy-agreements
- collection_type: open
  name: API Collection
  slug: open-godaddy-certificates
- collection_type: open
  name: Abuse Actions Contacts API
  slug: open-godaddy-contacts-api
- collection_type: open
  name: API Collection
  slug: open-godaddy-countries
- collection_type: open
  name: Abuse Actions Domains API
  slug: open-godaddy-domains-api
- collection_type: open
  name: Domains API
  slug: open-godaddy-domains
- collection_type: open
  name: 'Abuse Actions Expiry Auctions: Registrar Partners API'
  slug: open-godaddy-expiry-auctions-registrar-partners-api
- collection_type: open
  name: Abuse Actions Notifications API
  slug: open-godaddy-notifications-api
- collection_type: open
  name: API Collection
  slug: open-godaddy-orders
- collection_type: open
  name: API Collection
  slug: open-godaddy-shoppers
- collection_type: open
  name: API Collection
  slug: open-godaddy-subscriptions
- collection_type: open
  name: Abuse Actions v1 API
  slug: open-godaddy-v1-api
- collection_type: open
  name: Abuse Actions v2 API
  slug: open-godaddy-v2-api
common:
- group: commercial
  href: https://artifacts.apis.io/godaddy/plans/godaddy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/godaddy-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/godaddy/rate-limits/godaddy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/godaddy-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/godaddy/finops/godaddy-finops.yml
  title: ''
  type: FinOps
  url: finops/godaddy-finops.yml
- group: other
  href: https://artifacts.apis.io/godaddy/capabilities/godaddy-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/godaddy-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/godaddy/agentic-access/godaddy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/godaddy-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/godaddy/security/godaddy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/godaddy-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/godaddy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/godaddy
- group: company
  title: ''
  type: Website
  url: https://www.godaddy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.godaddy.com/doc
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.godaddy.com/getstarted
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.godaddy.com/legal/agreements/developer-api-terms
- group: operate
  title: ''
  type: Support
  url: https://developer.godaddy.com/support
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.godaddy.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.godaddy.com/resources/feed
created: '2026-03-16'
description: GoDaddy is a domain registrar and web hosting company offering REST APIs for domain registration, DNS management, certificates, shopper accounts, subscriptions, aftermarket auctions, and abuse reporting.
finops:
- has_sources: true
  method: generated
  name: Godaddy Finops
  primary_unit: ''
  service_category: Domains / DNS / Hosting
  slug: godaddy-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/godaddy.png
json_structures:
- name: Godaddy Structure
  property_count: 0
  slug: godaddy-structure
layout: provider
modified: '2026-05-19'
name: GoDaddy
nav: Providers
network: true
overview: 'GoDaddy publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Actions API, Contacts API, Domains API, and 16 more. Tagged areas include Aftermarket, Certificates, DNS, Domains, and Hosting.


  The GoDaddy catalog on APIs.io includes 1 Spectral governance ruleset.


  GoDaddy''s developer surface includes documentation, getting-started guide, support, engineering blog, and 11 more developer resources.'
plans:
- name: Godaddy Plans Pricing
  plan_count: 2
  slug: godaddy-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Godaddy Rate Limits
  slug: godaddy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: GoDaddy API Rules
  rule_count: 55
  severity_counts:
    error: 38
    hint: 0
    info: 4
    warn: 13
  slug: godaddy-rules
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.5
    catalog_earned_first_party: 0.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 48.7
    developer_ergonomics: 23.8
    discoverability: 78.6
    operational_transparency: 10.5
  previous_composite: 31.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 92.3
      derived: 0
      marker_coverage: 31.6
      total: 19
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/godaddy/godaddy-2026-06-20T181947.png
security:
- kind: domain-security
  name: Godaddy Domain Security
  slug: godaddy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: godaddy
tags:
- Aftermarket
- Certificates
- DNS
- Domains
- Hosting
- Registrar
website: https://www.godaddy.com/
---

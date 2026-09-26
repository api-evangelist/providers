---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://unstoppabledomains.com'', ''status'': 302, ''note'': ''declared website redirects to https://unstoppable.ai/ — a different registrable domain (unstoppabledomains.com -> unstoppable.ai), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: true
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.7
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 73
  human_in_the_loop: 5
  name: Unstoppable Domains Agentic Access
  operation_count: 136
  slug: unstoppable-domains-agentic-access
  summary_line: 136 operations · 73 acting · 5 human-in-the-loop
api_count: 4
apis:
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Manage your account details
  name: Unstoppable Domains Account API
  slug: unstoppable-domains-account-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Generate, manage, and remove AI-powered landing pages for domains (requires authentication)
  name: Unstoppable Domains AI Lander API
  slug: unstoppable-domains-ai-lander-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Create and manage domain backorders, and browse expired or pending-delete domains.
  name: Unstoppable Domains Backorders API
  slug: unstoppable-domains-backorders-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Shopping cart management, payment methods, and checkout (requires authentication)
  name: Unstoppable Domains Cart API
  slug: unstoppable-domains-cart-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Create and manage ICANN-required contacts for domain registration. Contacts represent individuals or organizations associated with domain roles (owner, admin, tech, billing). New contacts are automati
  name: Unstoppable Domains Contacts API
  slug: unstoppable-domains-contacts-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Manage DNS records, nameservers, and hosting configurations for owned domains (requires authentication)
  name: Unstoppable Domains DNS Management API
  slug: unstoppable-domains-dns-management-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Create, read, update and delete DNS records for your domains. Also includes DNS metadata, nameserver management, and DNSSEC configuration.
  name: Unstoppable Domains Dns Records API
  slug: unstoppable-domains-dns-records-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: View and update the ICANN-required contacts (owner, admin, tech, billing) assigned to a specific domain.
  name: Unstoppable Domains Domain Contacts API
  slug: unstoppable-domains-domain-contacts-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: View and manage domain flags that control behavior and security settings such as DNS resolution, transfer locks, WHOIS privacy, and more.
  name: Unstoppable Domains Domain Flags API
  slug: unstoppable-domains-domain-flags-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Comprehensive domain updates — modify nameservers, DNSSEC, contacts, flags, and DNS records in a single request.
  name: Unstoppable Domains Domain Management API
  slug: unstoppable-domains-domain-management-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Domain details/availability lookups and registration.
  name: Unstoppable Domains Domain Registration API
  slug: unstoppable-domains-domain-registration-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Search for domain availability and retrieve details for one or more domains. Use the `$expand` parameter to include registration details and flags in the response.
  name: Unstoppable Domains Domain Search API
  slug: unstoppable-domains-domain-search-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Check transfer eligibility and retrieve authorization codes for transferring domains to another registrar.
  name: Unstoppable Domains Domain Transfers API
  slug: unstoppable-domains-domain-transfers-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Manage your custody domains.
  name: Unstoppable Domains API
  slug: unstoppable-domains-domains-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: 'Manage domains that are owned in external, self-custody wallets. The key difference between Custody and Self-Custody operations is that all Self-Custody operations require a signature from the domain '
  name: Unstoppable Domains External Domains API
  slug: unstoppable-domains-external-domains-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: 'Manage self-custody wallets to allow for management of self-custody domains. ## Verifying Self-Custody Wallets Before you can initiate self-custody operations, you must first [verify the self-custody '
  name: Unstoppable Domains External Wallets API
  slug: unstoppable-domains-external-wallets-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Configure how your domains serve content on the web. Hosting configurations control what happens when someone visits your domain — whether it redirects to another URL or proxies content from another s
  name: Unstoppable Domains Hosting API
  slug: unstoppable-domains-hosting-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Domain conversations and messaging between buyers and sellers (requires authentication)
  name: Unstoppable Domains Leads API
  slug: unstoppable-domains-leads-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Browse and search the Unstoppable Domains secondary marketplace. Retrieve paginated listings of domains available for purchase from existing owners, with filtering by TLD and sorting options.
  name: Unstoppable Domains Marketplace API
  slug: unstoppable-domains-marketplace-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: All asynchronous processes handled by the API are represented as Operations. This includes registering a domain, updating a domain's records, changing a domain's owner, returning a domain and more.
  name: Unstoppable Domains Operations API
  slug: unstoppable-domains-operations-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: The Owner API from Unstoppable Domains — 1 operation(s) for owner.
  name: Unstoppable Domains Owner API
  slug: unstoppable-domains-owner-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Search for owned domains
  name: Unstoppable Domains Owners API
  slug: unstoppable-domains-owners-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Manage owned domains (requires authentication)
  name: Unstoppable Domains Portfolio API
  slug: unstoppable-domains-portfolio-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Retrieve pricing information for domain registration, renewal, transfer, and restoration by domain name or TLD.
  name: Unstoppable Domains Pricing API
  slug: unstoppable-domains-pricing-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: The Reverse API from Unstoppable Domains — 2 operation(s) for reverse.
  name: Unstoppable Domains Reverse API
  slug: unstoppable-domains-reverse-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: The Rpc Proxy API from Unstoppable Domains — 2 operation(s) for rpc proxy.
  name: Unstoppable Domains Rpc Proxy API
  slug: unstoppable-domains-rpc-proxy-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Search for owned entities
  name: Unstoppable Domains Search API
  slug: unstoppable-domains-search-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Generate authenticated browser URLs for account and checkout flows that require web handoff.
  name: Unstoppable Domains Session API
  slug: unstoppable-domains-session-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: The Status API from Unstoppable Domains — 2 operation(s) for status.
  name: Unstoppable Domains Status API
  slug: unstoppable-domains-status-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Suggestions for finding available domains
  name: Unstoppable Domains Suggestions API
  slug: unstoppable-domains-suggestions-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Browse available top-level domains (TLDs), their details, and DNS security configuration.
  name: Unstoppable Domains Tlds API
  slug: unstoppable-domains-tlds-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: Manage custody wallets used for storing and managing domains without any signature collection. These wallets provide the most streamlined way to interact with domains since the initial management requ
  name: Unstoppable Domains Wallets API
  slug: unstoppable-domains-wallets-api
- baseURL: https://api.unstoppabledomains.com/resolve
  baseurl_source: declared
  description: 'Manage webhooks used for asynchronous updates to your server. You can follow our getting started guide here: [Webhooks in the Partner API](https://docs.unstoppabledomains.com/domain-distribution-and-m'
  name: Unstoppable Domains Webhooks API
  slug: unstoppable-domains-webhooks-api
artifact_total: 74
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Web3 Partner API v3 account API
  slug: open-unstoppable-domains-account-api
- collection_type: open
  name: Web3 Partner API v3 account AI Lander API
  slug: open-unstoppable-domains-ai-lander-api
- collection_type: open
  name: Web3 Partner API v3 account Backorders API
  slug: open-unstoppable-domains-backorders-api
- collection_type: open
  name: Web3 Partner API v3 account Cart API
  slug: open-unstoppable-domains-cart-api
- collection_type: open
  name: Web3 Partner API v3 account contacts API
  slug: open-unstoppable-domains-contacts-api
- collection_type: open
  name: Web3 Partner API v3 account DNS Management API
  slug: open-unstoppable-domains-dns-management-api
- collection_type: open
  name: Web3 Partner API v3 account dns-records API
  slug: open-unstoppable-domains-dns-records-api
- collection_type: open
  name: Web3 Partner API v3 account domain-contacts API
  slug: open-unstoppable-domains-domain-contacts-api
- collection_type: open
  name: Web3 Partner API v3 account domain-flags API
  slug: open-unstoppable-domains-domain-flags-api
- collection_type: open
  name: Web3 Partner API v3 account domain-management API
  slug: open-unstoppable-domains-domain-management-api
- collection_type: open
  name: Web3 Partner API v3 account domain_registration API
  slug: open-unstoppable-domains-domain-registration-api
- collection_type: open
  name: Web3 Partner API v3 account domain-search API
  slug: open-unstoppable-domains-domain-search-api
- collection_type: open
  name: Web3 Partner API v3 account domain-transfers API
  slug: open-unstoppable-domains-domain-transfers-api
- collection_type: open
  name: Web3 Partner API v3 account domains API
  slug: open-unstoppable-domains-domains-api
- collection_type: open
  name: Web3 Partner API v3 account external_domains API
  slug: open-unstoppable-domains-external-domains-api
- collection_type: open
  name: Web3 Partner API v3 account external_wallets API
  slug: open-unstoppable-domains-external-wallets-api
- collection_type: open
  name: Web3 Partner API v3 account hosting API
  slug: open-unstoppable-domains-hosting-api
- collection_type: open
  name: Web3 Partner API v3 account Leads API
  slug: open-unstoppable-domains-leads-api
- collection_type: open
  name: Web3 Partner API v3 account marketplace API
  slug: open-unstoppable-domains-marketplace-api
- collection_type: open
  name: Web3 Partner API v3 account operations API
  slug: open-unstoppable-domains-operations-api
- collection_type: open
  name: Web3 Partner API v3 account Owner API
  slug: open-unstoppable-domains-owner-api
- collection_type: open
  name: Web3 Partner API v3 account owners API
  slug: open-unstoppable-domains-owners-api
- collection_type: open
  name: Web3 Partner API v3 account Portfolio API
  slug: open-unstoppable-domains-portfolio-api
- collection_type: open
  name: Web3 Partner API v3 account pricing API
  slug: open-unstoppable-domains-pricing-api
- collection_type: open
  name: Web3 Partner API v3 account Reverse API
  slug: open-unstoppable-domains-reverse-api
- collection_type: open
  name: Web3 Partner API v3 account Rpc Proxy API
  slug: open-unstoppable-domains-rpc-proxy-api
- collection_type: open
  name: Web3 Partner API v3 account search API
  slug: open-unstoppable-domains-search-api
- collection_type: open
  name: Web3 Partner API v3 account Session API
  slug: open-unstoppable-domains-session-api
- collection_type: open
  name: Web3 Partner API v3 account Status API
  slug: open-unstoppable-domains-status-api
- collection_type: open
  name: Web3 Partner API v3 account suggestions API
  slug: open-unstoppable-domains-suggestions-api
- collection_type: open
  name: Web3 Partner API v3 account tlds API
  slug: open-unstoppable-domains-tlds-api
- collection_type: open
  name: Web3 Partner API v3 account wallets API
  slug: open-unstoppable-domains-wallets-api
- collection_type: open
  name: Web3 Partner API v3 account webhooks API
  slug: open-unstoppable-domains-webhooks-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/unstoppable-domains/refs/heads/main/capabilities/unstoppable-domains-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/unstoppable-domains-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/unstoppable-domains/refs/heads/main/agentic-access/unstoppable-domains-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/unstoppable-domains-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/unstoppable-domains/refs/heads/main/security/unstoppable-domains-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/unstoppable-domains-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/unstoppable-domains/refs/heads/main/security/unstoppable-domains-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unstoppable-domains-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/unstoppable-domains/refs/heads/main/authentication/unstoppable-domains-authentication.yml
  title: ''
  type: Authentication
  url: authentication/unstoppable-domains-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://unstoppabledomains.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unstoppabledomains.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.unstoppabledomains.com/apis/overview
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/unstoppabledomains
- group: start
  title: ''
  type: Sandbox
  url: https://api.ud-sandbox.com
- group: auth
  title: ''
  type: Authentication
  url: https://docs.unstoppabledomains.com/domain-distribution-and-management/quickstart/retrieve-an-api-key
- group: commercial
  title: ''
  type: Pricing
  url: https://support.unstoppabledomains.com/support/solutions/articles/48001184253-pricing-tiers-for-regular-domains
- group: company
  title: ''
  type: Blog
  url: https://unstoppabledomains.com/blog
- group: other
  title: ''
  type: Developers
  url: https://unstoppabledomains.com/developers
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/unstoppable-domains/refs/heads/main/plans/unstoppable-domains-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/unstoppable-domains-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/unstoppable-domains/refs/heads/main/rate-limits/unstoppable-domains-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/unstoppable-domains-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/unstoppable-domains/refs/heads/main/finops/unstoppable-domains-finops.yml
  title: ''
  type: FinOps
  url: finops/unstoppable-domains-finops.yml
- group: other
  title: ''
  type: X
  url: https://x.com/unstoppableweb
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unstoppable-domains
created: '2026-06-14'
description: Web3 domain name service providing REST APIs for resolving crypto domain names, managing NFT domains, reverse lookups, cross-chain address resolution, domain registration, and DNS management across 150+ TLDs on multiple blockchains.
finops:
- name: Unstoppable Domains Finops
  service_category: ''
  slug: unstoppable-domains-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unstoppable-domains.png
layout: provider
modified: '2026-09-16'
name: Unstoppable Domains
nav: Providers
network: true
overview: 'Unstoppable Domains publishes 33 APIs on the [APIs.io](https://apis.io/) network, including Account API, AI Lander API, Backorders API, and 30 more. Tagged areas include Web3, Blockchain, Domain Names, NFT Domains, and Crypto.


  Unstoppable Domains'' developer surface includes authentication, documentation, API reference, sandbox, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Unstoppable Domains Plans Pricing
  plan_count: 4
  slug: unstoppable-domains-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Unstoppable Domains Rate Limits
  slug: unstoppable-domains-rate-limits
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 58.0
    catalog_earned_first_party: 0.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.4
  facets:
    access_clarity: 36.3
    contract_governance: 0.0
    contract_quality: 54.0
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 24.2
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 33
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/unstoppable-domains/refs/heads/main/screenshots/unstoppable-domains-2026-06-20T200411.png
security:
- kind: authentication
  name: Unstoppable Domains Authentication
  slug: unstoppable-domains-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Unstoppable Domains Domain Security
  slug: unstoppable-domains-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Unstoppable Domains Vulnerability Disclosure
  slug: unstoppable-domains-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: unstoppable-domains
tags:
- Web3
- Blockchain
- Domain Names
- NFT Domains
- Crypto
- Resolution
- DNS
- Decentralized
- Ethereum
- Polygon
website: https://unstoppabledomains.com
---

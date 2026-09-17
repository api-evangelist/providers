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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.0
  scored_at: '2026-09-16'
api_count: 2
apis:
- baseURL: https://domscan.net
  baseurl_source: declared
  description: The Agent Readiness API from DomScan — 1 operation(s) for agent readiness.
  name: DomScan Agent Readiness API
  slug: domscan-agent-readiness-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: The Batch API from DomScan — 4 operation(s) for batch.
  name: DomScan Batch API
  slug: domscan-batch-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: The Brand Protection API from DomScan — 5 operation(s) for brand protection.
  name: DomScan Brand Protection API
  slug: domscan-brand-protection-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Brand name quality scoring and comparison
  name: DomScan Brand Scoring API
  slug: domscan-brand-scoring-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Reference datasets and coverage metadata
  name: DomScan Dataset API
  slug: domscan-dataset-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: DNS record lookup, security analysis, and propagation checking
  name: DomScan DNS API
  slug: domscan-dns-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Review lookup-driven, day-level DNS observations from DomScan
  name: DomScan DNS History API
  slug: domscan-dns-history-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Check if domains are available for registration using RDAP
  name: DomScan Domain Availability API
  slug: domscan-domain-availability-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Comprehensive domain health analysis including DNS, SSL, and security
  name: DomScan Domain Health API
  slug: domscan-domain-health-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Domain comparison, scoring, popularity, lifecycle, and profile intelligence
  name: DomScan Domain Intelligence API
  slug: domscan-domain-intelligence-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Registration lifecycle, expiry, renewal, and deletion timing signals
  name: DomScan Domain Lifecycle API
  slug: domscan-domain-lifecycle-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: AI-powered domain name suggestions with availability checking
  name: DomScan Domain Suggestions API
  slug: domscan-domain-suggestions-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Algorithmic domain value estimation based on multiple factors
  name: DomScan Domain Valuation API
  slug: domscan-domain-valuation-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Email blacklist checking, disposable domain detection, and email validation
  name: DomScan Email API
  slug: domscan-email-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Build and validate SPF, DMARC, and DKIM records
  name: DomScan Email Authentication API
  slug: domscan-email-authentication-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Detect hosting providers, CDN, WAF, and email providers
  name: DomScan Hosting Detection API
  slug: domscan-hosting-detection-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Network and hosting infrastructure discovery
  name: DomScan Infrastructure API
  slug: domscan-infrastructure-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: IP geolocation, ASN lookup, and reverse DNS
  name: DomScan IP Intelligence API
  slug: domscan-ip-intelligence-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: API information and system endpoints
  name: DomScan Meta API
  slug: domscan-meta-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Open source intelligence tools for domain analysis
  name: DomScan OSINT API
  slug: domscan-osint-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Privacy-first phone number validation and formatting against bundled numbering-plan metadata
  name: DomScan Phone Intelligence API
  slug: domscan-phone-intelligence-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Scheduled standard-TLD rows from official sources and separate exact-domain quotes. Current public provider coverage and source scope are documented per integration.
  name: DomScan Pricing API
  slug: domscan-pricing-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Typed RDAP lookups and related registration analysis
  name: DomScan RDAP API
  slug: domscan-rdap-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Compound API endpoints bundling multiple services with credit savings
  name: DomScan Recipes API
  slug: domscan-recipes-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Security posture, reputation, exposure, and vulnerability intelligence
  name: DomScan Security API
  slug: domscan-security-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Social media handle availability checking
  name: DomScan Social API
  slug: domscan-social-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: SSL certificate grading, chain analysis, and expiry monitoring
  name: DomScan SSL Analysis API
  slug: domscan-ssl-analysis-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: TLS certificate, protocol, and transport security checks
  name: DomScan SSL API
  slug: domscan-ssl-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Certificate transparency search and subdomain discovery
  name: DomScan SSL Certificates API
  slug: domscan-ssl-certificates-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: TLD information, comparison, and coverage data
  name: DomScan TLD Intelligence API
  slug: domscan-tld-intelligence-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Detect typosquatting and brand impersonation risks
  name: DomScan Typosquatting API
  slug: domscan-typosquatting-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: API key management and usage statistics (requires login)
  name: DomScan User API
  slug: domscan-user-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Domain monitoring for expiration and availability (requires login)
  name: DomScan Watchlist API
  slug: domscan-watchlist-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Tech stack detection, categorization, and reputation
  name: DomScan Web Intelligence API
  slug: domscan-web-intelligence-api
- baseURL: https://domscan.net
  baseurl_source: declared
  description: Domain registration data lookup via RDAP and WHOIS
  name: DomScan WHOIS/RDAP API
  slug: domscan-whois-rdap-api
artifact_total: 43
asyncapis:
- description: ''
  name: Domscan Webhooks
  slug: domscan-webhooks
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://domscan.net/mcp
- group: company
  title: ''
  type: Website
  url: https://domscan.net
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/security/domscan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/domscan-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/authentication/domscan-authentication.yml
  title: ''
  type: Authentication
  url: authentication/domscan-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/well-known/domscan-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/domscan-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/mcp/domscan-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/domscan-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/scopes/domscan-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/domscan-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/errors/domscan-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/domscan-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/lifecycle/domscan-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/domscan-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/changelog/domscan-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/domscan-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/conventions/domscan-conventions.yml
  title: ''
  type: Conventions
  url: conventions/domscan-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/conventions/domscan-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/domscan-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/conformance/domscan-conformance.yml
  title: ''
  type: Conformance
  url: conformance/domscan-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/plans/domscan-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/domscan-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/rate-limits/domscan-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/domscan-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/data-model/domscan-data-model.yml
  title: ''
  type: DataModel
  url: data-model/domscan-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/cli/domscan-cli.yml
  title: ''
  type: CLI
  url: cli/domscan-cli.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/packages/domscan-packages.yml
  title: ''
  type: Packages
  url: packages/domscan-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/packages/domscan-packages.yml
  title: ''
  type: SDKs
  url: packages/domscan-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/asyncapi/domscan-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/domscan-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/overlays/domscan-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/domscan-openapi-overlay.yaml
- group: docs
  title: ''
  type: APIReference
  url: https://domscan.net/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://domscan.net/quickstart
- group: company
  title: ''
  type: Blog
  url: https://domscan.net/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://domscan.net/pricing
- group: start
  title: ''
  type: SignUp
  url: https://domscan.net/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://domscan.net/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://domscan.net/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/estevecastells
created: '2026-07-12'
description: Domain intelligence API for domain availability, DNS, WHOIS/RDAP, valuation, security checks, email posture, social handle checks, and monitoring workflows. Offers REST API, machine-readable contracts, a hosted MCP server, and llms.txt.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/domscan.png
layout: provider
mcp_servers:
- description: ''
  name: DomScan MCP Server
  slug: domscan-mcp-server
- description: Official hosted remote MCP server exposing 136 domain-intelligence tools (domain search, DNS, web intelligence, security, identity, monitoring, and workflow recipes) over Streamable HTTP. Works with C
  name: DomScan MCP Server
  slug: domscan-mcp-server-2
modified: '2026-09-03'
name: DomScan
nav: Providers
network: true
overview: 'DomScan publishes 35 APIs on the [APIs.io](https://apis.io/) network, including Agent Readiness API, Batch API, Brand Protection API, and 32 more. Tagged areas include Domains, DNS, WHOIS, rdap, and SSL/TLS.


  The DomScan catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DomScan''s developer surface includes authentication, changelog, CLI, API reference, getting-started guide, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Domscan Plans Pricing
  plan_count: 4
  slug: domscan-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Domscan Rate Limits
  slug: domscan-rate-limits
scopes:
- name: Domscan Scopes
  scope_count: 1
  slug: domscan-scopes
  summary_line: 1 scope
score:
  band: strong
  composite: 61.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.4
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 65.9
    developer_ergonomics: 63.7
    discoverability: 75.9
    operational_transparency: 57.9
  previous_composite: 56.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 35
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/screenshots/domscan-2026-07-25T212249.png
security:
- kind: authentication
  name: Domscan Authentication
  slug: domscan-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Domscan Domain Security
  slug: domscan-domain-security
  summary_line: TLSv1.3 · DMARC
slug: domscan
tags:
- Domains
- DNS
- WHOIS
- rdap
- SSL/TLS
- Email Security
- Domain Valuation
- Brand Protection
- OSINT
- Threat Intelligence
- MCP
- agent-native
website: https://domscan.net
---

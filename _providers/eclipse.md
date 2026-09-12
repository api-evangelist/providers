---
access_model:
  confidence: high
  label: Free · anonymous public read access
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
  - openapi
  - pricing
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-09-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Eclipse Agentic Access
  operation_count: 8
  slug: eclipse-agentic-access
  summary_line: 8 operations
api_count: 19
apis:
- baseURL: https://marketplace.eclipse.org
  baseurl_source: declared
  description: REST API for accessing Eclipse Marketplace data including listings, categories, favorites, and installation statistics for plugins, IDEs, and other extensions.
  name: Eclipse Marketplace API
  slug: marketplace-api
- baseURL: https://api.eclipse.org
  baseurl_source: declared
  description: Foundation-wide REST APIs for accessing project data, releases, committer paperwork, GeoIP, downloads, mailing lists, profiles, working groups, and other Eclipse Foundation services. Index of availabl
  name: Eclipse Foundation Web API
  slug: foundation-web-api
- baseURL: https://projects.eclipse.org
  baseurl_source: declared
  description: REST API exposing Eclipse Foundation project metadata, releases, committers, and project lifecycle data.
  name: Eclipse Projects API
  slug: projects-api
- baseURL: https://open-vsx.org
  baseurl_source: declared
  description: REST API for the Eclipse Open VSX Registry, an open-source alternative to the Visual Studio Marketplace for distributing VS Code-compatible extensions.
  name: Open VSX Registry API
  slug: open-vsx-api
- baseURL: https://newsroom.eclipse.org
  baseurl_source: declared
  description: REST API providing access to news, events, and announcements from the Eclipse Foundation newsroom.
  name: Eclipse Newsroom REST API
  slug: newsroom-api
- baseURL: https://marketplace.eclipse.org/api/p
  baseurl_source: declared
  description: The Eclipse Marketplace REST API API from Eclipse Foundation — 1 operation(s) for eclipse marketplace rest api.
  name: Eclipse Foundation Eclipse Marketplace REST API API
  slug: eclipse-eclipse-marketplace-rest-api-api
- baseURL: https://marketplace.eclipse.org/api/p
  baseurl_source: declared
  description: The Favorites API from Eclipse Foundation — 1 operation(s) for favorites.
  name: Eclipse Foundation Favorites API
  slug: eclipse-favorites-api
- baseURL: https://marketplace.eclipse.org/api/p
  baseurl_source: declared
  description: The Featured API from Eclipse Foundation — 1 operation(s) for featured.
  name: Eclipse Foundation Featured API
  slug: eclipse-featured-api
- baseURL: https://marketplace.eclipse.org/api/p
  baseurl_source: declared
  description: The Node API from Eclipse Foundation — 1 operation(s) for node.
  name: Eclipse Foundation Node API
  slug: eclipse-node-api
- baseURL: https://marketplace.eclipse.org/api/p
  baseurl_source: declared
  description: The Popular API from Eclipse Foundation — 1 operation(s) for popular.
  name: Eclipse Foundation Popular API
  slug: eclipse-popular-api
- baseURL: https://marketplace.eclipse.org/api/p
  baseurl_source: declared
  description: The Recent API from Eclipse Foundation — 1 operation(s) for recent.
  name: Eclipse Foundation Recent API
  slug: eclipse-recent-api
- baseURL: https://marketplace.eclipse.org/api/p
  baseurl_source: declared
  description: The Search API from Eclipse Foundation — 1 operation(s) for search.
  name: Eclipse Foundation Search API
  slug: eclipse-search-api
- baseURL: https://marketplace.eclipse.org/api/p
  baseurl_source: declared
  description: The Taxonomy API from Eclipse Foundation — 1 operation(s) for taxonomy.
  name: Eclipse Foundation Taxonomy API
  slug: eclipse-taxonomy-api
- baseURL: https://api.eclipse.org/download
  baseurl_source: declared
  description: REST API for Eclipse Foundation release and download metadata — active release trains, release versions and individual file records used to drive the eclipse.org download pages and mirror selection.
  name: Eclipse Foundation Downloads API
  slug: downloads-api
- baseURL: https://api.eclipse.org/geoip
  baseurl_source: declared
  description: REST API resolving a client IP address to a country, city or country IP-range set. Used by the Eclipse Foundation to select download mirrors and regionalise content.
  name: Eclipse GeoIP REST API
  slug: geoip-api
- baseURL: https://api.eclipse.org/git
  baseurl_source: declared
  description: REST API that validates Git contributions against the Eclipse Contributor Agreement. Exposes ECA lookup and commit validation as a callable service, plus inbound GitHub and GitLab webhook receivers us
  name: Eclipse Foundation Git ECA API
  slug: git-eca-api
- baseURL: https://api.eclipse.org/foundation/info
  baseurl_source: declared
  description: REST API exposing Eclipse Foundation reference data — board members, registered trademarks and CVE records — plus a Slack membership webhook receiver.
  name: Eclipse Foundation Info API
  slug: info-api
- baseURL: https://api.eclipse.org/foundation/mailing-list
  baseurl_source: declared
  description: REST API for Eclipse Foundation mailing list metadata and subscription records, authenticated against the auth.eclipse.org foundation realm.
  name: Eclipse Foundation Mailing List API
  slug: mailing-lists-api
- baseURL: https://api.eclipse.org
  baseurl_source: declared
  description: REST API for Eclipse account profiles and user metadata, including the two-phase user deletion request flow the Foundation operates for data-protection erasure requests.
  name: Eclipse Profile API
  slug: profile-api
- baseURL: https://api.eclipse.org/working-groups
  baseurl_source: declared
  description: REST API for Eclipse working groups and special interest groups — participation levels, resources, participation agreements and committee membership.
  name: Eclipse Working Groups API
  slug: working-groups-api
- baseURL: https://api.eclipse.org/foundation/paperwork
  baseurl_source: declared
  description: REST API for Eclipse committer paperwork records, authenticated against the auth.eclipse.org document-signature realm with dedicated committer_paperwork_retrieve, _update and _delete scopes.
  name: Eclipse Committer Paperwork API
  slug: committer-paperwork-api
- baseURL: https://api.eclipse.org/foundation/hellosign
  baseurl_source: declared
  description: REST API wrapping Dropbox Sign (HelloSign) for Eclipse Foundation document signing — signature requests for committer paperwork, membership and working-group agreements — plus the inbound signature ev
  name: Eclipse HelloSign API
  slug: hellosign-api
- baseURL: https://membership.eclipse.org/api
  baseurl_source: declared
  description: REST API for the Eclipse Foundation membership portal — member organisations, contacts, products, yearly activity, industry collaborations, project and working-group relations. The largest OIDC-protec
  name: Eclipse Membership Portal API
  slug: membership-portal-api
- baseURL: https://membership.eclipse.org/application_api
  baseurl_source: declared
  description: REST API backing the Eclipse Foundation membership application forms — form creation, contacts, organizations, working-group selections and submission.
  name: Eclipse Membership Application API
  slug: membership-application-api
- baseURL: https://api.eclipse.org/openvsx
  baseurl_source: declared
  description: REST API for submitting and revoking the Eclipse Open VSX publisher agreement against an Eclipse account, gated by the openvsx_publisher_agreement OAuth scope.
  name: Eclipse Open VSX Publisher Agreement API
  slug: openvsx-agreement-api
- baseURL: https://api.eclipse.org/adopters
  baseurl_source: declared
  description: REST API listing the organisations that have declared adoption of an Eclipse Foundation project, per project or across the whole estate.
  name: Eclipse Project Adopters API
  slug: project-adopters-api
artifact_total: 45
asyncapis:
- description: ''
  name: Eclipse Webhooks
  slug: eclipse-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Eclipse Marketplace REST Eclipse Marketplace REST API API
  slug: open-eclipse-eclipse-marketplace-rest-api-api
- collection_type: open
  name: Eclipse Marketplace REST Eclipse Marketplace REST API Favorites API
  slug: open-eclipse-favorites-api
- collection_type: open
  name: Eclipse Marketplace REST Eclipse Marketplace REST API Featured API
  slug: open-eclipse-featured-api
- collection_type: open
  name: Eclipse Marketplace REST Eclipse Marketplace REST API Node API
  slug: open-eclipse-node-api
- collection_type: open
  name: Eclipse Marketplace REST Eclipse Marketplace REST API Popular API
  slug: open-eclipse-popular-api
- collection_type: open
  name: Eclipse Marketplace REST Eclipse Marketplace REST API Recent API
  slug: open-eclipse-recent-api
- collection_type: open
  name: Eclipse Marketplace REST Eclipse Marketplace REST API Search API
  slug: open-eclipse-search-api
- collection_type: open
  name: Eclipse Marketplace REST Eclipse Marketplace REST API Taxonomy API
  slug: open-eclipse-taxonomy-api
- collection_type: open
  name: Eclipse Marketplace REST API
  slug: open-eclipse
common:
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/eclipse-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eclipse-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.eclipse.org/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eclipse-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/eclipse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eclipse-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eclipse-foundation
- group: start
  title: ''
  type: Portal
  url: https://www.eclipse.org/
- group: docs
  title: ''
  type: API Documentation Index
  url: https://webdev.eclipse.org/docs/api/
- group: company
  title: ''
  type: Blog
  url: https://blogs.eclipse.org/
- group: company
  title: ''
  type: News
  url: https://newsroom.eclipse.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eclipse
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eclipse.org/legal/termsofuse.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eclipse.org/legal/privacy.php
- group: commercial
  title: ''
  type: License
  url: https://www.eclipse.org/legal/epl-2.0/
- group: build
  title: ''
  type: Packages
  url: packages/eclipse-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/eclipse-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/eclipse-cli.yml
- group: design
  title: ''
  type: Components
  url: components/eclipse-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/eclipse-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/eclipse-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eclipse-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/eclipse-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eclipse-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eclipse-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.eclipse.org
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/eclipse-lifecycle.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://auth.eclipse.org/auth/realms/foundation/.well-known/openid-configuration
- group: auth
  title: ''
  type: Security
  url: https://www.eclipse.org/security/policy/
- group: design
  title: ''
  type: Conventions
  url: conventions/eclipse-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/eclipse-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/eclipse-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eclipse-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/eclipse-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/eclipse-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/eclipse-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/eclipse-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://webdev.eclipse.org/docs/api/
- group: docs
  title: ''
  type: Documentation
  url: https://webdev.eclipse.org/docs/api/
- group: docs
  title: ''
  type: APIReference
  url: https://webdev.eclipse.org/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.eclipse.org/projects/handbook/
- group: operate
  title: ''
  type: Support
  url: https://www.eclipse.org/org/foundation/contact.php
- group: start
  title: ''
  type: SignUp
  url: https://accounts.eclipse.org/user/register
- group: start
  title: ''
  type: Login
  url: https://accounts.eclipse.org/user/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.eclipse.org/membership/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/eclipse-openvsx/openvsx
created: '2024-01-01'
description: 'The Eclipse Foundation is a non-profit (Belgian AISBL) that provides a global community of individuals and organizations with a mature, scalable and business-friendly environment for open source software collaboration and innovation. It is also a substantial API provider in its own right: it publishes 294 REST operations across 18 first-party OpenAPI specifications, covering Eclipse project and release metadata (Projects PMI), the Eclipse Marketplace, the Eclipse Newsroom, Foundation downloads and GeoIP, Eclipse Contributor Agreement validation, committer paperwork and document signing, mailing lists, member organizations and working groups, Eclipse account profiles, and the Eclipse Open VSX Registry — the vendor-neutral marketplace for VS Code-compatible extensions, which also implements the Microsoft VS Code Extension Gallery wire protocol. Read access across the entire surface is anonymous, unmetered and free; writes authenticate against Keycloak OpenID Connect on auth.eclipse.org
  or, for Open VSX publishing, a personal access token.'
finops:
- name: Eclipse Finops
  service_category: API
  slug: eclipse-finops
image: https://www.eclipse.org/eclipse.org-common/themes/solstice/public/images/logo/eclipse-foundation-grey-orange.svg
layout: provider
modified: '2026-09-07'
name: Eclipse Foundation
nav: Providers
network: true
overview: 'Eclipse Foundation publishes 26 APIs on the [APIs.io](https://apis.io/) network, including Eclipse Marketplace API, Web API, Eclipse Projects API, and 23 more. Tagged areas include Eclipse Foundation, Foundation, Open-Source, Standards, and Developer-Tools.


  The Eclipse Foundation catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Eclipse Foundation''s developer surface includes authentication, developer portal, engineering blog, product news, CLI, changelog, documentation, and 40 more developer resources.'
plans:
- name: Eclipse Plans Pricing
  plan_count: 0
  slug: eclipse-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Eclipse Rate Limits
  slug: eclipse-rate-limits
scopes:
- name: Eclipse Scopes
  scope_count: 11
  slug: eclipse-scopes
  summary_line: 11 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 61.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 59.3
    developer_ergonomics: 73.2
    discoverability: 81.5
    operational_transparency: 52.6
  previous_composite: 61.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 26
    mcp: derived
    skills: derived
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://raw.githubusercontent.com/api-evangelist/eclipse/refs/heads/main/screenshots/eclipse-2026-06-20T180424.png
security:
- kind: authentication
  name: Eclipse Authentication
  slug: eclipse-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Eclipse Domain Security
  slug: eclipse-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Eclipse Vulnerability Disclosure
  slug: eclipse-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: eclipse
tags:
- Eclipse Foundation
- Foundation
- Open-Source
- Standards
- Developer-Tools
- Extensions
- Marketplace
- Registry
- Governance
- Java
- IDE
- Project-Metadata
website: https://www.eclipse.org/
---

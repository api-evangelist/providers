---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Brandfolder Agentic Access
  operation_count: 73
  slug: brandfolder-agentic-access
  summary_line: 73 operations · 38 acting
api_count: 1
apis:
- baseURL: https://brandfolder.com/api/v4
  baseurl_source: declared
  description: Assets are the core resource of Brandfolder. They act like containers that hold all of your digital resources and files, which we call Attachments. They belong to a Section in a Brandfolder and can al
  name: Brandfolder Assets API
  slug: brandfolder-assets-api
- baseURL: https://brandfolder.com/api/v4
  baseurl_source: declared
  description: Attachments are the representation of digital assets in Brandfolder. Generally speaking, they are actual files but can also be colors, fonts, links to embedded/external media, etc. They belong to an A
  name: Brandfolder Attachments API
  slug: brandfolder-attachments-api
- baseURL: https://brandfolder.com/api/v4
  baseurl_source: declared
  description: 'Brandfolder''s Binary Upload service allows for authenticated users to upload locally stored files into Brandfolder via our API. Binary Upload is a multi-step process: 1. [Get an upload URL](/api/brand'
  name: Brandfolder Binary Upload API
  slug: brandfolder-binary-upload-api
- baseURL: https://brandfolder.com/api/v4
  baseurl_source: declared
  description: Brandfolders are nested directly underneath an Organization in the overall heirarchy. They can have many Collections, Sections, and Assets.
  name: Brandfolder Brandfolders API
  slug: brandfolder-brandfolders-api
- baseURL: https://brandfolder.com/api/v4
  baseurl_source: declared
  description: Collections are nested under a Brandfolder and contain many Assets. They are mainly used as an additional way to organize, manage, share, and restrict access to a subset of Assets within your Brandfol
  name: Brandfolder Collections API
  slug: brandfolder-collections-api
- baseURL: https://brandfolder.com/api/v4
  baseurl_source: declared
  description: Custom Fields can be assigned to Assets and are generally helpful for organizing and searching Assets within a Brandfolder, as well as for understanding more details about each Asset. Each Custom Fiel
  name: Brandfolder Custom Fields API
  slug: brandfolder-custom-fields-api
- baseURL: https://brandfolder.com/api/v4
  baseurl_source: declared
  description: Invitations are exactly what they sound like and can be created to invite Users to join your Organization, Brandfolder, or Collection as a `guest`, `collaborator`, `admin`, or (when inviting someone t
  name: Brandfolder Invitations API
  slug: brandfolder-invitations-api
- baseURL: https://brandfolder.com/api/v4
  baseurl_source: declared
  description: Brandfolder's Labels are an enhanced organization and findability feature meant to provide the peace of mind that comes with an organization's existing folder structure. Think of Labels like your musi
  name: Brandfolder Labels API
  slug: brandfolder-labels-api
- baseURL: https://brandfolder.com/api/v4
  baseurl_source: declared
  description: An Organization is the top level resource of all objects in Brandfolder. It can have many Brandfolders nested beneath it.
  name: Brandfolder Organizations API
  slug: brandfolder-organizations-api
- baseURL: https://brandfolder.com/api/v4
  baseurl_source: declared
  description: 'Sections are nested under a Brandfolder and contain many Assets. They exist to help keep Assets organized within a Brandfolder. They also determine which type of digital assets can be uploaded within '
  name: Brandfolder Sections API
  slug: brandfolder-sections-api
- baseURL: https://brandfolder.com/api/v4
  baseurl_source: declared
  description: 'Tags can be assigned to Assets and are generally helpful for organizing and searching Assets within a Brandfolder. Each Tag is essentially a keyword associated with exactly one Asset. For example, if '
  name: Brandfolder Tags API
  slug: brandfolder-tags-api
- baseURL: https://brandfolder.com/api/v4
  baseurl_source: declared
  description: User permissions describe relationships between Organizations, Brandfolders, Collections, Portals or Brandguides and the users that have access to them. Learn more about permissioning in our Knowledge
  name: Brandfolder User Permissions API
  slug: brandfolder-user-permissions-api
- baseURL: https://brandfolder.com/api/v4
  baseurl_source: declared
  description: The Brandfolder Webhooks service allows you to subscribe to event-based notifications (callbacks) when a qualifying event is triggered within Brandfolder. Asset data will then be sent to the user-prov
  name: Brandfolder Webhooks API
  slug: brandfolder-webhooks-api
artifact_total: 24
asyncapis:
- description: ''
  name: Brandfolder Webhooks
  slug: brandfolder-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/brandfolder-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/brandfolder-openapi-original-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/brandfolder-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/brandfolder-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brandfolder-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/brandfolder-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brandfolder-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brandfolder.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.smartsheet.com/api/brandfolder
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brandfolder
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brandfolder-inc-
- group: company
  title: ''
  type: Blog
  url: https://brandfolder.engineering/
- group: commercial
  title: ''
  type: Pricing
  url: https://brandfolder.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.brandfolder.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/Brandfolder
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.smartsheet.com/api/brandfolder
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.smartsheet.com/api/brandfolder/introduction
- group: operate
  title: ''
  type: Support
  url: https://help.smartsheet.com/brandfolder
- group: operate
  title: ''
  type: Community
  url: https://community.smartsheet.com/
- group: start
  title: ''
  type: Login
  url: https://brandfolder.com/signin/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.smartsheet.com/legal/user-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.smartsheet.com/legal/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.smartsheet.com/legal/bugbounty
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/brandfolder-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.smartsheet.com/legal/security
- group: design
  title: ''
  type: Conformance
  url: conformance/brandfolder-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/brandfolder-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/brandfolder-packages.yml
- group: design
  title: ''
  type: Components
  url: components/brandfolder-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/brandfolder-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/brandfolder-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/brandfolder-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brandfolder-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/brandfolder-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/brandfolder-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/brandfolder-finops.yml
created: 2026-06-13
description: Brandfolder is a digital asset management (DAM) platform and Smartsheet company that provides a RESTful API for managing brand assets, collections, sections, tags, share links, webhooks, and asset distribution permissions. The API enables organizations to push Brandfolder content to other applications, pull data from external sources, and synchronize Brandfolder with other platforms.
finops:
- name: Brandfolder Finops
  service_category: ''
  slug: brandfolder-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brandfolder.png
jsonld:
- class_count: 0
  name: Brandfolder Context
  property_count: 13
  slug: brandfolder-context
layout: provider
mcp_servers:
- description: ''
  name: Brandfolder MCP Server
  slug: brandfolder-mcp-server
modified: 2026-08-13
name: Brandfolder
nav: Providers
network: true
overview: 'Brandfolder publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Attachments API, Binary Upload API, and 10 more. Tagged areas include Digital Asset Management, DAM, Brand Management, Assets, and Media.


  The Brandfolder catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Brandfolder''s developer surface includes authentication, documentation, engineering blog, pricing, getting-started guide, support, changelog, and 30 more developer resources.'
plans:
- name: Brandfolder Plans Pricing
  plan_count: 2
  slug: brandfolder-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Brandfolder Rate Limits
  slug: brandfolder-rate-limits
score:
  band: strong
  composite: 55.5
  coverage:
    artifact_dirs: 25
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 82.9
    commercial_clarity: 82.9
    contract_governance: 4.5
    contract_quality: 66.5
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 36.8
  previous_composite: 55.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brandfolder/refs/heads/main/screenshots/brandfolder-2026-06-20T173633.png
security:
- kind: authentication
  name: Brandfolder Authentication
  slug: brandfolder-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Brandfolder Domain Security
  slug: brandfolder-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Brandfolder Vulnerability Disclosure
  slug: brandfolder-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Brandfolder Trust Center
  slug: brandfolder-trust-center
  summary_line: SOC 2, HIPAA
slug: brandfolder
tags:
- Digital Asset Management
- DAM
- Brand Management
- Assets
- Media
- Collection
- Smartsheet
website: https://brandfolder.com
---

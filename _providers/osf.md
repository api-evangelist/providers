---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Open Science Framework API v2 provides programmatic access to projects, registrations, files, and other research resources.
  name: OSF API
  slug: osf-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: Actions represent state transitions or comments performed on reviewable or request-related resources within the OSF platform, such as Preprints, Nodes, Preprint Requests, Node Requests, and Collection
  name: OSF Actions API
  slug: osf-actions-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: '**OAuth2 Applications** allow external services to securely authenticate and interact with OSF resources via OAuth2. Registered applications manage OAuth2 flows, client credentials, and access tokens.'
  name: OSF Applications API
  slug: osf-applications-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: This is the "home page" of the API you can get important autentication information for the user making the request and get links to other resources.
  name: OSF Base API
  slug: osf-base-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: CEDAR Metadata endpoints allow you to create, read, update, and manage metadata records based on CEDAR templates. These templates enable users to apply structured, standardized metadata to nodes and f
  name: OSF CEDAR Metadata API
  slug: osf-cedar-metadata-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: The Citations API from OSF — 2 operation(s) for citations.
  name: OSF Citations API
  slug: osf-citations-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: A Collection Submissions Provider represents the data for moderators and admins for a group of collections. It acts as a central hub for managing all collection submissions within various collections,
  name: OSF Collection Providers API
  slug: osf-collection-providers-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: The Collection Submission Actions API from OSF — 2 operation(s) for collection submission actions.
  name: OSF Collection Submission Actions API
  slug: osf-collection-submission-actions-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: A Collection Submission is an object that allows a user to add a resource, either a project, preprint, or registration to a collection. Once created, a Collection Submission may be automatically accep
  name: OSF Collection Submissions API
  slug: osf-collection-submissions-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: The Collections API from OSF — 11 operation(s) for collections.
  name: OSF Collections API
  slug: osf-collections-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: The Comments API from OSF — 1 operation(s) for comments.
  name: OSF Comments API
  slug: osf-comments-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: The Contributors API from OSF — 1 operation(s) for contributors.
  name: OSF Contributors API
  slug: osf-contributors-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: Custom Metadata endpoints allow users to manage freeform or structured metadata associated with OSF nodes and files. Unlike CEDAR metadata, Custom Metadata provides more flexible fields tailored to sp
  name: OSF Custom Metadata API
  slug: osf-custom-metadata-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: A Draft Registration is a object that allows a user to edit and revise a registration before it is registered. Draft Registrations allow contributors to coordinate on a single registration, so they ca
  name: OSF Draft Registrations API
  slug: osf-draft-registrations-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: The Files API from OSF — 5 operation(s) for files.
  name: OSF Files API
  slug: osf-files-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: The GUIDs API from OSF — 1 operation(s) for guids.
  name: OSF GUIDs API
  slug: osf-guids-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: Identifiers are unique strings associated with various entities in the OSF system, such as project nodes, registrations or preprints. Identifiers serve as a means to distinctly reference these entitie
  name: OSF Identifiers API
  slug: osf-identifiers-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: The Institutions API from OSF — 8 operation(s) for institutions.
  name: OSF Institutions API
  slug: osf-institutions-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: The Licenses API from OSF — 2 operation(s) for licenses.
  name: OSF Licenses API
  slug: osf-licenses-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: The Logs API from OSF — 2 operation(s) for logs.
  name: OSF Logs API
  slug: osf-logs-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: The Nodes API from OSF — 37 operation(s) for nodes.
  name: OSF Nodes API
  slug: osf-nodes-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: '**Notification Subscriptions** allow users to manage how they receive alerts about activities and events related to OSF resources, such as projects, preprints, registrations, and collections. Subscrip'
  name: OSF Notification Subscriptions API
  slug: osf-notification-subscriptions-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: OAuth scopes define specific permissions for OAuth applications and personal access tokens. Each scope indicates the permission level granted to perform actions via the OSF API, such as reading node d
  name: OSF OAuth Scopes API
  slug: osf-oauth-scopes-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: Preprint Providers are entities that manage and moderate groups of preprints on the OSF platform. Each Preprint Provider oversees its own preprint service, which can include branding, theming, subject
  name: OSF Preprint Providers API
  slug: osf-preprint-providers-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: The Preprints API from OSF — 17 operation(s) for preprints.
  name: OSF Preprints API
  slug: osf-preprints-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: Storage Regions are predefined geographical or cloud-storage areas where files are stored within OSF Storage. Each region provides isolation of data in compliance with geographic or regulatory require
  name: OSF Regions API
  slug: osf-regions-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: Registration Providers are entities that manage and moderate groups of registrations on the OSF platform. Each Registration Provider defines workflows, review policies, and customization options for t
  name: OSF Registration Providers API
  slug: osf-registration-providers-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: 'Registration Schema Blocks are read-only entities, they represent question prompts and form inputs known as "blocks" that make up a Registration Schemas. Each block has a designated `block_type` that '
  name: OSF Registration Schema Blocks API
  slug: osf-registration-schema-blocks-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: A Registration Schemas defines the range of valid responses to a registration. Each Registration Schema is composed of <a href="#tag/Registration-Schema-Blocks">"blocks"</a> that define the individual
  name: OSF Registration Schemas API
  slug: osf-registration-schemas-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: The Registrations API from OSF — 38 operation(s) for registrations.
  name: OSF Registrations API
  slug: osf-registrations-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: Manage user-initiated requests related to nodes and preprints, including access requests, withdrawal requests, and institutional affiliation requests. Requests are actions initiated by users to either
  name: OSF Requests API
  slug: osf-requests-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: 'Resources are structured data artifacts associated with a Registration. These can include datasets, analytic code, materials, papers, or supplementary files that contribute to the outcomes of a study '
  name: OSF Resources API
  slug: osf-resources-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: Schema Response Actions are objects that when created cause state transitions for Schema Responses. Users use state transitions to submit, approve, and revise new Schema Responses. Schema Response Act
  name: OSF Schema Response Actions API
  slug: osf-schema-response-actions-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: Schema Responses contain user supplied responses to a Registration Schema. A Schema Response aggregates all of the the responses for a given version of a Registration's Registration Schema. Schema Res
  name: OSF Schema Responses API
  slug: osf-schema-responses-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: Subjects endpoints provide access to the taxonomy used for categorizing OSF resources such as nodes, preprints, and registrations. Subjects can be hierarchical, with parent and child relationships, al
  name: OSF Subjects API
  slug: osf-subjects-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: The Taxonomies API from OSF — 4 operation(s) for taxonomies.
  name: OSF Taxonomies API
  slug: osf-taxonomies-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: '**Personal Access Tokens** allow users to authenticate API requests without credentials. Tokens support fine-grained permissions (scopes) to control API access levels.'
  name: OSF Tokens API
  slug: osf-tokens-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: Users represent individual accounts within the OSF (Open Science Framework) platform. Each user account includes identifying information such as names, email addresses, profile details, and metadata a
  name: OSF Users API
  slug: osf-users-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: The View Only Links API from OSF — 2 operation(s) for view only links.
  name: OSF View Only Links API
  slug: osf-view-only-links-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: The Wikis endpoints allow users to create, update, retrieve, and manage wiki pages and their versions for OSF projects and registrations. Wikis are collaborative documents that enable teams to share i
  name: OSF Wikis API
  slug: osf-wikis-api
- baseURL: https://api.osf.io
  baseurl_source: declared
  description: Addons represent a user connection to an external service, some addons allow for additional storage, some modify user authentication or add a redirect link to a project.
  name: OSF Add Ons API
  slug: osf-add-ons-api
artifact_total: 43
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/osf/refs/heads/main/rules/osf-rules.yml
  title: ''
  type: Spectral
  url: rules/osf-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/osf/refs/heads/main/vocabulary/osf-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/osf-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/osf/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/osf/refs/heads/main/errors/osf-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/osf-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/osf/refs/heads/main/conformance/osf-conformance.yml
  title: ''
  type: Conformance
  url: conformance/osf-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/osf/refs/heads/main/hosts/osf-hosts.yml
  title: ''
  type: Hosts
  url: hosts/osf-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/osf/refs/heads/main/vendors/osf-vendors.yml
  title: ''
  type: Vendors
  url: vendors/osf-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://help.osf.io/collection/331-getting-started-live-training-and-recording-library
- group: docs
  title: ''
  type: Documentation
  url: https://developer.osf.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/osf/refs/heads/main/security/osf-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/osf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://osf.io
- group: docs
  title: ''
  type: APIReference
  url: https://developer.osf.io
- group: operate
  title: ''
  type: Support
  url: https://osf.io
- group: company
  title: ''
  type: Blog
  url: https://www.cos.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/centerforopenscience
- group: operate
  title: ''
  type: Roadmap
  url: https://www.cos.io/initiatives/top-guidelines
- group: commercial
  title: ''
  type: Pricing
  url: https://osf.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://osf.io/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://osf.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://osf.io/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/centerforopenscience/workspace/osf
created: '2026-10-13'
description: OSF (Open Science Framework) is a free, open-source platform that supports the entire research lifecycle, enabling collaboration, data sharing, and reproducible workflows. Researchers can register projects, collect data, manage materials, and publish results, all while integrating with tools like Dropbox, GitHub, and more. The platform emphasizes openness, inclusivity, and long-term preservation of scholarly outputs.
layout: provider
modified: '2026-10-13'
name: OSF
nav: Providers
network: true
overview: 'OSF publishes 41 API contracts indexed on the [APIs.io](https://apis.io/) network, including Actions API, Applications API, Base API, and 38 more. Tagged areas include Company, Open Science, Research, Collaboration, and Platform.


  The OSF catalog on APIs.io includes 1 Spectral governance ruleset.


  OSF''s developer surface includes getting-started guide, documentation, API reference, support, engineering blog, pricing, signup flow, and 14 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: OSF API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 2
  slug: osf-rules
score:
  band: developing
  composite: 42.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 40.8
    catalog_earned_first_party: 0.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 35.6
    contract_quality: 48.4
    developer_ergonomics: 46.9
    discoverability: 62.5
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 40
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Osf Domain Security
  slug: osf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: osf
tags:
- Company
- Open Science
- Research
- Collaboration
- Platform
- Open Source
website: https://osf.io
---

---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 99
  human_in_the_loop: 0
  name: Mri Software Agentic Access
  operation_count: 190
  slug: mri-software-agentic-access
  summary_line: 190 operations · 99 acting
api_count: 1
apis:
- description: An open and connected ecosystem of secure REST APIs built by MRI and its partners that enables controlled data exchange between MRI's core property management and accounting platform and third-party o
  name: MRI Information Exchange (MIX) API
  slug: mri-information-exchange-api
- description: REST APIs providing programmatic access to MRI's core property management platform, covering residential and commercial property portfolios, units, leases, resident ledgers, maintenance work orders, a
  name: MRI Property Management X API
  slug: mri-property-management-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>All asset types are associated with an asset group. An asset group connects asset types that have similar characteristics. Use the API to retrieve a list of all asset groups, add or update, or dele
  name: MRI Software Asset groups API
  slug: mri-software-asset-groups-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>Manage the movement of assets using the API. Retrieve a list of all asset movements, view a specific movement, and update an movement.</p><p>Learn more about assets in the <a href='https://onlocati
  name: MRI Software Asset movements API
  slug: mri-software-asset-movements-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>An asset type is a subset of an asset group. Use the API to retrieve a list of all asset types, add or update, or delete an asset type.</p><p>Learn more about assets in the <a href='https://onlocat
  name: MRI Software Asset types API
  slug: mri-software-asset-types-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>Manage your organization’s assets with OnLocation. Use the API to retrieve a list of assets, add or update, or delete an asset, or issue or return an asset. Your account owner must first enable the
  name: MRI Software Assets API
  slug: mri-software-assets-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>When records are created, updated or deleted within your account, an audit log is created. Use the audit log API to retrieve the last 30 days worth of data corresponding to changes within your acco
  name: MRI Software Audit log API
  slug: mri-software-audit-log-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>Each certification added to an employee or contractor profile can have a document attached. Use the API to return a list of certification documents, and update or delete a certification document.</
  name: MRI Software Certification holder documents API
  slug: mri-software-certification-holder-documents-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: '<p>Certifications can be assigned to employees and contractors. Each certification record includes the dates that the certification is valid for, along with the person''s name, email, and if there are '
  name: MRI Software Certification holders API
  slug: mri-software-certification-holders-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>Certification types are used to group similar types of certifications, for example qualifications, certificates, licenses, degrees. Use the API to return the full list of certification types, or ad
  name: MRI Software Certification types API
  slug: mri-software-certification-types-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>Certifications are used to record employee and contractor accreditations in OnLocation. Use the API to retrieve the certifications created for your organization, add or update, or delete a certific
  name: MRI Software Certifications API
  slug: mri-software-certifications-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: The Communities API from MRI Software — 2 operation(s) for communities.
  name: MRI Software Communities API
  slug: mri-software-communities-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: The Community field list API from MRI Software — 1 operation(s) for community field list.
  name: MRI Software Community field list API
  slug: mri-software-community-field-list-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: The Community field tabs API from MRI Software — 1 operation(s) for community field tabs.
  name: MRI Software Community field tabs API
  slug: mri-software-community-field-tabs-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: The Community member movements API from MRI Software — 2 operation(s) for community member movements.
  name: MRI Software Community member movements API
  slug: mri-software-community-member-movements-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: The CommunityMembers API from MRI Software — 2 operation(s) for communitymembers.
  name: MRI Software Community Members API
  slug: mri-software-communitymembers-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>Contractor contact role types are used to categorize contractor members. Use the API to retrieve a list of role types set up at your organization.</p><p>Learn more about role types in the <a href='
  name: MRI Software Contractor contact role types API
  slug: mri-software-contractor-contact-role-types-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>Contractor organization insurance policies can have documents attached to them. Use the API to retrieve a list of all documents attached to a policy, add new documents, and update or delete existin
  name: MRI Software Contractor insurance documents API
  slug: mri-software-contractor-insurance-documents-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>Insurance management in OnLocation is used to manage contractor organizations' insurance policies. Use the API to retrieve a list of all insurance policies, add new ones, and update or delete exist
  name: MRI Software Contractor insurance policies API
  slug: mri-software-contractor-insurance-policies-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>Each time a contractor signs in or out, they create a movement. Use the API to return all contractor member movements, or add or update a movement record.</p>
  name: MRI Software Contractor member movements API
  slug: mri-software-contractor-member-movements-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>A contractor member belongs to an organization that is contracted to provide a service. Each member has a profile in OnLocation that includes their contact details, status, access permission dates,
  name: MRI Software Contractor members API
  slug: mri-software-contractor-members-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>Each contractor organization has individual members that are authorized to work on-site. A contractor member can belong to multiple contractor organizations in OnLocation.</p> <p>Use the API to ret
  name: MRI Software Contractor membership API
  slug: mri-software-contractor-membership-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: '<p>Categories are used to describe the different functions of your contractor organizations. You can use them to sort your organizations and make it easier to report on them and create triggers. </p> '
  name: MRI Software Contractor organization categories API
  slug: mri-software-contractor-organization-categories-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>Groups are a subset of contractor organization categories. For example, electrical, cleaning, and maintenance could be groups under the facilities category. They are used to organize your organizat
  name: MRI Software Contractor organization groups API
  slug: mri-software-contractor-organization-groups-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>A contractor organization is contracted to provide a service. Each organization has a profile in OnLocation that includes contact information, status, location access, insurance policies, and linke
  name: MRI Software Contractor organizations API
  slug: mri-software-contractor-organizations-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>Users can add new tabs to organize the custom fields in their employee or contractor profiles. Use the custom fields API to retrieve any employee, contractor organization, and contractor member cus
  name: MRI Software Custom field tabs API
  slug: mri-software-custom-field-tabs-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>Custom fields are used to record information that is not covered by the the default employee and contractor profile fields. Use the custom fields API to retrieve any employee custom fields, contrac
  name: MRI Software Custom fields API
  slug: mri-software-custom-fields-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>When someone answers a custom question in a questionnaire submission, OnLocation records their submission and links it to the questionnaire submission ID and custom question ID.</p><p>Use the API t
  name: MRI Software Custom question answers API
  slug: mri-software-custom-question-answers-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: Returns a list of all custom questionnaire submissions (excluding the answers). Includes location, kiosk, who submitted the answer, where the movement took place, date and time.
  name: MRI Software Custom questionnaire submissions API
  slug: mri-software-custom-questionnaire-submissions-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>A custom questionnaire is a set of custom questions that are asked during sign in, sign out, or visitor pre-registration. The custom questionnaire API retrieves your custom questionnaires and can r
  name: MRI Software Custom questionnaires API
  slug: mri-software-custom-questionnaires-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>A custom questionnaire is made up of a set of custom questions. Use the API to list all custom questions created for your organization. View details including the question type (eg multi-choice, wa
  name: MRI Software Custom questions API
  slug: mri-software-custom-questions-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>Each time an employee signs in or out, or moves between zones, they create a movement. Use the API to return all employee movements, or add or update a movement record.</p>
  name: MRI Software Employee movements API
  slug: mri-software-employee-movements-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>Each employee has a profile in OnLocation. It contains their name, contact information, locations, department, user roles and role types, and tokens.</p></p>Use the employee API to return a list of
  name: MRI Software Employees API
  slug: mri-software-employees-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: '<p>Induction courses are to record if an employee or contractor has completed required training. There are four types of induction course in OnLocation: internal, external, eLearning and SCORM Cloud. '
  name: MRI Software Induction courses API
  slug: mri-software-induction-courses-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>An induction holder is someone who has completed an induction course. Induction holder records include the learner's name, email, status of the course, the number of attempts, when it's due to be r
  name: MRI Software Induction holders API
  slug: mri-software-induction-holders-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>Departments are used to assign employees to different operational areas of a location. Use the API to retrieve a list of all departments, create new departments and the locations they apply to, upd
  name: MRI Software Location departments API
  slug: mri-software-location-departments-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>Zone groups are used to group your location's zones together. For example, a zone group may be a building and each floor is a zone. Use the API to retrieve a list of all zone groups, add new zone g
  name: MRI Software Location zone groups API
  slug: mri-software-location-zone-groups-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>Zones are used to split your location into specific areas. If you use the Desks and Spaces add-on, you can also create bookable workspaces within each zone. Use the API to retrieve a list of all zo
  name: MRI Software Location zones API
  slug: mri-software-location-zones-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>Each OnLocation account is made up of one or more locations. A location record contains the name, contact details, timezone, date format, employee count, and the access points set up for that locat
  name: MRI Software Locations API
  slug: mri-software-locations-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: OnLocation sends email, SMS, and OnLocation Mobile push notifications. Use the notification API to retrieve a list of all notifications and provide a notification ID to retrieve a single notification.
  name: MRI Software Notifications API
  slug: mri-software-notifications-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>A pre-registered visitor is someone who has been approved by an employee to visit a location. Each visitor is linked to a visit event. Use the pre-registered visitor API to retrieve your pre-regist
  name: MRI Software Pre-registered visitors API
  slug: mri-software-pre-registered-visitors-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: The qualifications endpoints have been deprecated as Qualifications Management has been renamed Certifications Management. Use the <a href='/openapi/wol/tag/Certification-holder-documents/'>certificat
  name: MRI Software Qualification holder documents (deprecated) API
  slug: mri-software-qualification-holder-documents-deprecated-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: The qualifications endpoints have been deprecated as Qualifications Management has been renamed Certifications Management. Use the <a href='/openapi/wol/tag/Certification-holders/'>certification holde
  name: MRI Software Qualification holders (deprecated) API
  slug: mri-software-qualification-holders-deprecated-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: The qualifications endpoints have been deprecated as Qualifications Management has been renamed Certifications Management. Use the <a href='/openapi/wol/tag/Certification-types/'>certification types</
  name: MRI Software Qualification types (deprecated) API
  slug: mri-software-qualification-types-deprecated-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: The qualifications endpoints have been deprecated as Qualifications Management has been renamed Certifications Management. Use the <a href='/openapi/wol/tag/Certifications/'>certifications</a> endpoin
  name: MRI Software Qualifications (deprecated) API
  slug: mri-software-qualifications-deprecated-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>Each employee can maintain a saved visitor list in OnLocation. Use the saved visitor API to retrieve all saved visitors, add a new saved visitor, or update or delete a saved visitor.</p><p>Learn mo
  name: MRI Software Saved visitors API
  slug: mri-software-saved-visitors-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>A visitor event is a record listing the details of a visit, including the visitor's name, where they visited, contact details, basic question answers, and sign in/out mode and time.</p><p>Use the v
  name: MRI Software Visitor events API
  slug: mri-software-visitor-events-api
- baseURL: https://api.whosonlocation.com/v1
  baseurl_source: declared
  description: <p>Each visitor group is created by an employee and includes a set of their visitors who are pre-registered to attend the same events. Use the visitor group API to retrieve your visitor group list, ad
  name: MRI Software Visitor groups API
  slug: mri-software-visitor-groups-api
artifact_total: 65
common:
- group: other
  href: https://artifacts.apis.io/mri-software/capabilities/mri-software-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mri-software-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/mri-software/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/mri-software/agentic-access/mri-software-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mri-software-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/mri-software/rules/mri-software-rules.yml
  title: ''
  type: Spectral
  url: rules/mri-software-rules.yml
- group: design
  href: https://artifacts.apis.io/mri-software/json-ld/mri-software-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mri-software-context.jsonld
- group: design
  href: https://artifacts.apis.io/mri-software/vocabulary/mri-software-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mri-software-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mri-software/data-model/mri-software-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mri-software-data-model.yml
- group: operate
  href: https://artifacts.apis.io/mri-software/changelog/mri-software-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mri-software-changelog.yml
- group: design
  href: https://artifacts.apis.io/mri-software/conventions/mri-software-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mri-software-conventions.yml
- group: auth
  href: https://artifacts.apis.io/mri-software/authentication/mri-software-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mri-software-authentication.yml
- group: auth
  href: https://artifacts.apis.io/mri-software/scopes/mri-software-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/mri-software-scopes.yml
- group: design
  href: https://artifacts.apis.io/mri-software/lifecycle/mri-software-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mri-software-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/mri-software/errors/mri-software-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mri-software-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mri-software/conformance/mri-software-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mri-software-conformance.yml
- group: other
  href: https://artifacts.apis.io/mri-software/overlays/mri-software-onlocation-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mri-software-onlocation-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/mri-software/well-known/mri-software-statuspage-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mri-software-statuspage-security.txt
- group: auth
  href: https://artifacts.apis.io/mri-software/well-known/mri-software-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mri-software-status-security.txt
- group: agent
  href: https://artifacts.apis.io/mri-software/well-known/mri-software-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mri-software-well-known.yml
- group: other
  href: https://artifacts.apis.io/mri-software/hosts/mri-software-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mri-software-hosts.yml
- group: build
  href: https://artifacts.apis.io/mri-software/integrations/mri-software-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/mri-software-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/mri-software/vendors/mri-software-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mri-software-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mrisoftware.com/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://www.mrisoftware.com/contact-support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mrisoftware.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.mrisoftware.com/news/
- group: start
  title: ''
  type: Login
  url: https://www.mrisoftware.com/login/
- group: other
  title: ''
  type: Leadership
  url: https://www.mrisoftware.com/leadership/
- group: auth
  href: https://artifacts.apis.io/mri-software/security/mri-software-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mri-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mrisoftware.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mrisoftware.com/mrifunctionalspecs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/MRI-Software
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mri-software-llc
- group: company
  title: ''
  type: Blog
  url: https://www.mrisoftware.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mrisoftware.com/products/onlocation/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mrisoftware.com/
- group: other
  title: ''
  type: X
  url: https://x.com/mrisoftware
- group: commercial
  href: https://artifacts.apis.io/mri-software/plans/mri-software-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mri-software-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/mri-software/rate-limits/mri-software-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mri-software-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/mri-software/finops/mri-software-finops.yml
  title: ''
  type: FinOps
  url: finops/mri-software-finops.yml
created: '2026-06-13'
description: MRI Software is a real estate technology platform serving over 45,000 clients across 170+ countries. It provides REST APIs and an open integration ecosystem for property management, investment management, lease accounting, facilities management, visitor and contractor management, and commercial real estate analytics. The MRI Information Exchange (MIX) hosts over 1,000 vetted APIs for data exchange between MRI's core platform and third-party or custom applications.
finops:
- has_sources: false
  method: generated
  name: Mri Software Finops
  primary_unit: ''
  service_category: ''
  slug: mri-software-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mri-software.png
json_schemas:
- name: CommunityMemberMovementResponse
  property_count: 31
  slug: mri-software-community-member-movement-response
- name: ContractorMovementRequest
  property_count: 23
  slug: mri-software-contractor-movement-request
- name: ContractorMovementResponse
  property_count: 48
  slug: mri-software-contractor-movement-response
- name: ContractorOrganisationRequest
  property_count: 13
  slug: mri-software-contractor-organisation-request
- name: StaffMovementResponse
  property_count: 34
  slug: mri-software-staff-movement-response
- name: VisitorEventResponse
  property_count: 41
  slug: mri-software-visitor-event-response
jsonld:
- class_count: 89
  name: Mri Software Context
  property_count: 262
  slug: mri-software-context
layout: provider
modified: '2026-10-20'
name: MRI Software
nav: Providers
network: true
overview: 'MRI Software publishes 48 API contracts indexed on the [APIs.io](https://apis.io/) network, including Asset groups API, Asset movements API, Asset types API, and 45 more. Tagged areas include Real Estate, Property Management, Investment Management, Lease Accounting, and Facilities Management.


  The MRI Software catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MRI Software''s developer surface includes changelog, authentication, support, documentation, engineering blog, pricing, and 33 more developer resources.'
plans:
- name: Mri Software Plans Pricing
  plan_count: 5
  slug: mri-software-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Mri Software Rate Limits
  slug: mri-software-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: MRI Software API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 2
  slug: mri-software-rules
scopes:
- name: Mri Software Scopes
  scope_count: 2
  slug: mri-software-scopes
  summary_line: 2 scopes
score:
  band: strong
  composite: 57.4
  coverage:
    artifact_dirs: 31
    catalog_earned: 68.8
    catalog_earned_first_party: 8.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 46.1
    contract_governance: 22.0
    contract_quality: 63.9
    developer_ergonomics: 37.5
    discoverability: 58.9
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 61.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 46
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/mri-software/mri-software-2026-06-20T185841.png
security:
- kind: authentication
  name: Mri Software Authentication
  slug: mri-software-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Mri Software Domain Security
  slug: mri-software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: pre-register-visitor
  slug: mri-software-pre-register-visitor
- name: sync-employees
  slug: mri-software-sync-employees
slug: mri-software
tags:
- Real Estate
- Property Management
- Investment Management
- Lease Accounting
- Facilities Management
- Commercial Real Estate
- Visitor Management
- PropTech
website: https://www.mrisoftware.com/
---

---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Checkr Agentic Access
  operation_count: 60
  slug: checkr-agentic-access
  summary_line: 60 operations · 25 acting
api_count: 1
apis:
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Account and user metadata.
  name: Checkr Account API
  slug: checkr-account-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: FCRA adverse action workflows against a report.
  name: Checkr Adverse Actions API
  slug: checkr-adverse-actions-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Candidate records that background checks are run against.
  name: Checkr Candidates API
  slug: checkr-candidates-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Ongoing monitoring for new records.
  name: Checkr Continuous Checks API
  slug: checkr-continuous-checks-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Files attached to a candidate.
  name: Checkr Documents API
  slug: checkr-documents-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: State/locale definitions scoping pricing and compliance.
  name: Checkr Geos API
  slug: checkr-geos-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Hosted invitations for candidates to submit their own information.
  name: Checkr Invitations API
  slug: checkr-invitations-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Bundles of screenings and the programs that group them.
  name: Checkr Packages API
  slug: checkr-packages-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: The container aggregating a candidate's screenings and result.
  name: Checkr Reports API
  slug: checkr-reports-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Recurring re-runs of a package for a candidate.
  name: Checkr Subscriptions API
  slug: checkr-subscriptions-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Education and employment verification screenings.
  name: Checkr Verifications API
  slug: checkr-verifications-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Event notification subscriptions.
  name: Checkr Webhooks API
  slug: checkr-webhooks-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Adverse Items are items selected from a returned report that may be used to initiate Adverse Action for a Candidate.
  name: Checkr Adverse Items API
  slug: checkr-adverse-items-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: 'Use this endpoint to return the Assessments for Reports. <b>Note: </b>Listen to the `report.updated` webhook to determine when an Assessment has been applied to a report.'
  name: Checkr Assessments API
  slug: checkr-assessments-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: The candidate postal address is the address Checkr will use to send postal mail to the candidate. Each candidate can be associated with only one postal address.
  name: Checkr Candidate Postal Address API
  slug: checkr-candidate-postal-address-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: 'Candidate Stories allows candidates with records the opportunity to share additional context about themselves and their background checks. Once submitted, these stories will be available to customers '
  name: Checkr Candidate Stories API
  slug: checkr-candidate-stories-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: The Counties resource provides a list of all counties within the United States. Use the returned list to validate the counties submitted by your candidates during the [Self Disclosure](#operation/crea
  name: Checkr Counties API
  slug: checkr-counties-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: County Criminal records make up the majority of criminal records, and are therefore one of the most complete sources for both felony and misdemeanor records. These records are not reported to the fede
  name: Checkr County Criminal Search API
  slug: checkr-county-criminal-search-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: The driver licenses resource represents a single driver license for a candidate. Candidates may have one current driver license and may have any number of previous driver licenses.
  name: Checkr Driver Licenses API
  slug: checkr-driver-licenses-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: A Drug & Alcohol Clearinghouse search provides information about a candidate's drug and alcohol violation history. The screening includes a query result of Driver Prohibited or Not Prohibited. Further
  name: Checkr Drug & Alcohol Clearinghouse Search API
  slug: checkr-drug-alcohol-clearinghouse-search-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Use an Education Verification to verify a candidate’s education history, and highest degree achieved. For this screening, candidates are asked to supply their degree, major, school, and the state in w
  name: Checkr Education Verification API
  slug: checkr-education-verification-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: The Employers resource includes all relevant employer information for the specified Candidate. Employer resources are tied to the specified candidate, and do not transfer to other employees within the
  name: Checkr Employers API
  slug: checkr-employers-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Use an Employment Verification to verify a candidate’s employment history for the last three employers, or the last seven years. For this screening, candidates are asked to supply their employment his
  name: Checkr Employment Verification API
  slug: checkr-employment-verification-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Searches databases for records of adverse actions against individuals and entities in the healthcare field. For more information, please see [FACIS](https://help.checkr.com/hc/en-us/articles/360001576
  name: Checkr FACIS Search API
  slug: checkr-facis-search-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Searches the PACER database to identify Federal Civil records. Checkr conducts Federal District Searches to verify records identified by this search. For more information, please see [Federal Civil Di
  name: Checkr Federal Civil Search API
  slug: checkr-federal-civil-search-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Searches the Federal Criminal record database and Federal District courts to return felony and misdemeanor records. (National, State, and County Criminal Searches do not return federal records.) For m
  name: Checkr Federal Criminal Search API
  slug: checkr-federal-criminal-search-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Searches Federal District Civil courts to verify felony and misdemeanor records identified by PACER For more information, please see [Federal District Civil Search](https://help.checkr.com/hc/en-us/ar
  name: Checkr Federal District Civil Search API
  slug: checkr-federal-district-civil-search-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Searches Federal District Criminal courts to verify felony and misdemeanor records identified by PACER. For more information, please see [Federal District Criminal Search](https://help.checkr.com/hc/e
  name: Checkr Federal District Criminal Search API
  slug: checkr-federal-district-criminal-search-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: The Forms I-9 resource provides all information about Forms I-9. It also allows to create a new Form I-9, retrieves details about ongoing I-9s (creating a CSV file) and also makes the PDF files for co
  name: Checkr Forms I-9 API
  slug: checkr-forms-i-9-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: The Global Watchlist Search searches known domestic and international terrorist watchlists as well as the records of the Office of Inspector General (OIG), Excluded Parties List (EPL) and additional d
  name: Checkr Global Watchlist Search API
  slug: checkr-global-watchlist-search-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: 'Use the Hierarchy endpoint to structure your Account as a grouping of individual entities (Nodes) that represent your business with respect to your hiring and background check needs. The parent-child '
  name: Checkr Hierarchy (Enabled by request) API
  slug: checkr-hierarchy-enabled-by-request-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: 'In countries where third party access to criminal record information is restricted, Adverse Media Checks may be performed to access private databases, public sanctions lists, media sources, and other '
  name: Checkr International Adverse Media Search API
  slug: checkr-international-adverse-media-search-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Criminal records check in supported countries. Criminal data is accessed from the appropriate database or agency. Refer to [International Screenings](https://help.checkr.com/hc/en-us/articles/36005610
  name: Checkr International Criminal Search API
  slug: checkr-international-criminal-search-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: The verification of academic status of any educational level such as high school, college and post-grad may include institution name, dates of attendance, graduation/conferred date, degree obtained, m
  name: Checkr International Education Verification API
  slug: checkr-international-education-verification-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Verification of previous employment history may include employer’s name, dates of employment, position/title, reason for leaving, eligibility for rehire, and comments. Reasonable attempts will be made
  name: Checkr International Employment Verification API
  slug: checkr-international-employment-verification-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: 'A comprehensive search of multiple U.S. and International government watchlists which include the FBI’s Most Wanted list, Interpol''s Most Wanted lists, Office of Foreign Asset Control Sanction lists, '
  name: Checkr International Global Watchlist Search API
  slug: checkr-international-global-watchlist-search-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Verifies that the candidate’s passport, national ID or driver’s license is authentic and validly in circulation. This check provides a multi-level validation process by inspecting document data and po
  name: Checkr International Identity Document Validation API
  slug: checkr-international-identity-document-validation-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Checks the validity of a driver license and where available, may include a detailed history of the candidate’s driving violations or license conditions. Canada only at this time. Refer to [Internation
  name: Checkr International Motor Vehicle Report API
  slug: checkr-international-motor-vehicle-report-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: 'Motor Vehicle Records originate from a state’s Department of Motor Vehicles, and include information related to a person’s driving history, including driver’s license status and restrictions, as well '
  name: Checkr Motor Vehicle Report API
  slug: checkr-motor-vehicle-report-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Checkr conducts a National Criminal Database Search as a routine part of all criminal background checks. The search queries 3,200 counties and over 900 million records across the United States, and pr
  name: Checkr National Criminal Search API
  slug: checkr-national-criminal-search-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Nodes are the individual entities that comprise an Account Hierarchy. If hierarchy is enabled for your Checkr Account, this endpoint may be used to retrieve a list of all Account Nodes. To create Node
  name: Checkr Nodes API
  slug: checkr-nodes-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Use a Personal Reference Verification to verify a candidate’s personal credentials. For this screening, candidates are asked to supply a personal reference. Checkr then contacts the personal reference
  name: Checkr Personal Reference Verification API
  slug: checkr-personal-reference-verification-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Use a Professional License Verification to verify a candidate's professional credentials.
  name: Checkr Professional License Verification API
  slug: checkr-professional-license-verification-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: The professional license resource represents a single certification or license issued to a candidate for qualification in a professional field. Candidates may have two existing professional license re
  name: Checkr Professional Licenses API
  slug: checkr-professional-licenses-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Use a Professional Reference Verification to verify a candidate’s professional credentials. For this screening, candidates are asked to supply a professional reference. Checkr then contacts the profes
  name: Checkr Professional Reference Verification API
  slug: checkr-professional-reference-verification-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Represents a division of an Account. Programs are typically used to identify clients, cost centers, or departments. A Program may have many Geos and may have many Packages.
  name: Checkr Programs API
  slug: checkr-programs-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Represents candidate reported addresses on a Report.
  name: Checkr Report Addresses API
  slug: checkr-report-addresses-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Report ETAs predict when screenings will complete for each background check report. This ETA provides a date for the estimated completion of a specific report, helping both you and your candidates pla
  name: Checkr Report ETA API
  slug: checkr-report-eta-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Report Tags are defined by customers, and may be used to search Reports.
  name: Checkr Report Tags API
  slug: checkr-report-tags-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: The School resource includes all relevant educational information for the specified Candidate. School resources are tied to the specified candidate, and do not transfer to other alumna within the syst
  name: Checkr Schools API
  slug: checkr-schools-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: Represents an instant multi-state Sex Offender Registry Search. A nationwide search of all 50 states' and the District of Columbia’s sex offender registries for all levels of registered sex offenders.
  name: Checkr Sex Offender Registry Search API
  slug: checkr-sex-offender-registry-search-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: 'The SSN resource allows you to retrieve a candidate''s encrypted SSN. **Note**: Access to this endpoint requires an RSA key-pair for encryption. See [Configuring Encryption for Candidate SSN Endpoint]('
  name: Checkr SSN API
  slug: checkr-ssn-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: 'SSN Trace is typically the first screening run, and is used to verify that the input SSN exists, determine where and when it was issued, and to compile a list of all known aliases associated with the '
  name: Checkr SSN Trace API
  slug: checkr-ssn-trace-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: 'The State Criminal Search returns criminal records from a selected state’s database, the content of which varies by state. Some states include records reported from all counties; some include records '
  name: Checkr State Criminal Search API
  slug: checkr-state-criminal-search-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: The User resource includes user information and role assignments. Users can be invited and assigned roles from the Dashboard.
  name: Checkr Users API
  slug: checkr-users-api
- baseURL: https://api.checkr.com/v1
  baseurl_source: declared
  description: The User resource includes user information and role assignments. Users can be invited and assigned roles from the Dashboard.
  name: Checkr Worksites API
  slug: checkr-worksites-api
artifact_total: 80
collections:
- collection_type: open
  name: Checkr Account API
  slug: open-checkr-account-api
- collection_type: open
  name: Checkr Account Adverse Actions API
  slug: open-checkr-adverse-actions-api
- collection_type: open
  name: Checkr Account Candidates API
  slug: open-checkr-candidates-api
- collection_type: open
  name: Checkr Account Continuous Checks API
  slug: open-checkr-continuous-checks-api
- collection_type: open
  name: Checkr Account Documents API
  slug: open-checkr-documents-api
- collection_type: open
  name: Checkr Account Geos API
  slug: open-checkr-geos-api
- collection_type: open
  name: Checkr Account Invitations API
  slug: open-checkr-invitations-api
- collection_type: open
  name: Checkr Account Nodes and Hierarchy API
  slug: open-checkr-nodes-and-hierarchy-api
- collection_type: open
  name: Checkr Account Packages API
  slug: open-checkr-packages-api
- collection_type: open
  name: Checkr Account Reports API
  slug: open-checkr-reports-api
- collection_type: open
  name: Checkr Account Screenings API
  slug: open-checkr-screenings-api
- collection_type: open
  name: Checkr Account Subscriptions API
  slug: open-checkr-subscriptions-api
- collection_type: open
  name: Checkr Account Verifications API
  slug: open-checkr-verifications-api
- collection_type: open
  name: Checkr Account Webhooks API
  slug: open-checkr-webhooks-api
- collection_type: open
  name: Checkr API
  slug: open-checkr
common:
- group: company
  title: ''
  type: Blog
  url: https://checkr.com/blog
- group: other
  href: https://artifacts.apis.io/checkr/capabilities/checkr-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/checkr-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/checkr/agentic-access/checkr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/checkr-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/checkr/security/checkr-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/checkr-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/checkr/security/checkr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/checkr-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/checkr/authentication/checkr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/checkr-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/checkr
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/checkr
- group: company
  title: ''
  type: Website
  url: https://checkr.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.checkr.com/
- group: commercial
  href: https://artifacts.apis.io/checkr/plans/checkr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/checkr-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/checkr/rate-limits/checkr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/checkr-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/checkr/finops/checkr-finops.yml
  title: ''
  type: FinOps
  url: finops/checkr-finops.yml
created: '2026-07-03'
description: Checkr is a technology-driven background check platform for employment screening. Its REST API lets employers, staffing firms, and platform partners run compliant background checks programmatically - creating candidates, sending invitations, ordering packages, and retrieving reports composed of individual screenings (SSN trace, county/state/national/federal criminal searches, sex offender registry, motor vehicle records, education and employment verifications, and more). The API also covers adverse action workflows, continuous checks and subscriptions, node/hierarchy and geo account structure, Form I-9, documents, and webhooks for event-driven report status updates. Authentication is HTTP Basic auth with a secret API key, with OAuth for Checkr Partner integrations.
finops:
- has_sources: true
  method: generated
  name: Checkr Finops
  primary_unit: ''
  service_category: Background Screening and Compliance
  slug: checkr-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/checkr.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.checkr.com over HTTP.
  name: Checkr MCP Server
  slug: checkr
modified: '2026-10-06'
name: Checkr
nav: Providers
network: true
overview: 'Checkr publishes 56 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Adverse Actions API, Candidates API, and 53 more. Tagged areas include Background Checks, Employment Screening, Compliance, Human Resources, and Identity Verification.


  The Checkr catalog on APIs.io includes 1 Spectral governance ruleset.


  Checkr''s developer surface includes engineering blog, authentication, documentation, and 10 more developer resources.'
plans:
- name: Checkr Plans Pricing
  plan_count: 5
  slug: checkr-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Checkr Rate Limits
  slug: checkr-rate-limits
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Checkr API Rules
  rule_count: 66
  severity_counts:
    error: 53
    hint: 0
    info: 1
    warn: 12
  slug: checkr-rules
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 59.2
    developer_ergonomics: 32.1
    discoverability: 68.3
    operational_transparency: 7.9
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 78.9
      total: 71
    mcp: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/checkr/checkr-2026-07-25T205136.png
security:
- kind: authentication
  name: Checkr Authentication
  slug: checkr-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Checkr Domain Security
  slug: checkr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Checkr Trust Center
  slug: checkr-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: checkr
tags:
- Background Checks
- Employment Screening
- Compliance
- Human Resources
- Identity Verification
- Criminal Records
- Recruiting
website: https://checkr.com
---

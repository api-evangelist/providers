---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-09-16'
api_count: 19
apis:
- description: The University's own API developer portal and gateway — a self-hosted Gravitee API Management deployment. The portal REST API answers anonymously and is, in practice, the University's API discovery su
  name: University of Helsinki API Portal (Gravitee)
  slug: api-gateway
- description: SBOM upload to the University's Dependency Track instance from external networks. Public and running in the portal, but publishes no OpenAPI page, so no contract is stored here.
  name: Dependency Track
  slug: dependency-track
- description: Liferay headless delivery API for Flamma, the staff intranet, distributed through the University gateway. No OpenAPI page is published; the upstream contract is Liferay's.
  name: Flamma Liferay Headless API
  slug: flamma-liferay-headless
- description: Authenticated access to the Drupal JSON:API behind the internal guide, covering published and unpublished content. No OpenAPI page is published.
  name: Internal Guide CMS JSON-API
  slug: internal-guide-cms
- description: Public HAL REST API for Helda, the University's open institutional repository, running DSpace 7.6.2. Discovery/search, items, collections, communities and the metadata registry are all readable anonym
  name: Helda DSpace REST API
  slug: helda-rest
- description: OAI-PMH 2.0 harvesting endpoint for Helda. Identify returns repositoryName "Helda" with an earliest datestamp of 1976-05-13, and ListMetadataFormats returns fourteen prefixes — oai_dc, qdc, qdc_helda,
  name: Helda OAI-PMH Metadata Interface
  slug: helda-oai
- description: 'A SECOND, separate DSpace deployment — datakatalogi.helsinki.fi, running DSpace 9.0 with dspaceName "HyDatacatalogue" — cataloguing research DATA rather than publications. New: its OAI earliest datest'
  name: HY Data Catalogue DSpace REST API
  slug: datakatalogi-rest
- description: OAI-PMH 2.0 endpoint for the HY Data Catalogue. Identify returns repositoryName "HyDatacatalogue", adminEmail datakatalogi@helsinki.fi, granularity YYYY-MM-DDThh:mm:ssZ. Institution-operated and anony
  name: HY Data Catalogue OAI-PMH Interface
  slug: datakatalogi-oai
- description: OAI-PMH 2.0 endpoint for Editori, the University's open publishing service (PKP Open Journal Systems). Identify returns repositoryName "Editori - Avoimen julkaisemisen palvelu", adminEmail editori@hel
  name: Editori (journals.helsinki.fi) OAI-PMH Interface
  slug: editori-oai
- description: 'The University''s identity provider at login.helsinki.fi, machine-readable twice over. SAML: GET /idp/shibboleth returns an EntityDescriptor with entityID https://login.helsinki.fi/shibboleth, an IDPSS'
  name: HY Login Service — Shibboleth IdP + OpenID Connect
  slug: identity-provider
- description: TENANT RELATIONSHIP, NOT A UNIVERSITY CONTRACT. The University runs its own instance of Sisu, the student information system built by Funidata Oy and shared across Finnish universities, at sisu.helsin
  name: Sisu (Kori) Student Information System — University of Helsinki tenant
  slug: sisu-kori
- description: TENANT RELATIONSHIP. researchportal.helsinki.fi is an Elsevier Pure deployment (the page markup identifies Pure and Elsevier directly). It is the University's research information system and its conte
  name: University of Helsinki Research Portal — Elsevier Pure tenant
  slug: research-portal
- description: TENANT RELATIONSHIP. helka.helsinki.fi redirects to an Ex Libris Primo discovery interface with view identifier 358UOH_INST:VU1. Library discovery is the surface class that is almost always a vendor's
  name: Helka Library Discovery — Ex Libris Primo tenant
  slug: helka
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The AllNodeAttributes API from University of Helsinki — 1 operation(s) for allnodeattributes.
  name: University of Helsinki All Node Attributes API
  slug: university-of-helsinki-allnodeattributes-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The AllSuccessorsAndPredecessors API from University of Helsinki — 1 operation(s) for allsuccessorsandpredecessors.
  name: University of Helsinki All Successors And Predecessors API
  slug: university-of-helsinki-allsuccessorsandpredecessors-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Annotations API from University of Helsinki — 3 operation(s) for annotations.
  name: University of Helsinki Annotations API
  slug: university-of-helsinki-annotations-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: dawasync API rest service
  name: University of Helsinki /api API
  slug: university-of-helsinki-api-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The API user API from University of Helsinki — 3 operation(s) for api user.
  name: University of Helsinki API user API
  slug: university-of-helsinki-api-user-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Areas API from University of Helsinki — 2 operation(s) for areas.
  name: University of Helsinki Areas API
  slug: university-of-helsinki-areas-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Audio API from University of Helsinki — 7 operation(s) for audio.
  name: University of Helsinki Audio API
  slug: university-of-helsinki-audio-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Authentication event API from University of Helsinki — 1 operation(s) for authentication event.
  name: University of Helsinki Authentication event API
  slug: university-of-helsinki-authentication-event-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Autocomplete API from University of Helsinki — 3 operation(s) for autocomplete.
  name: University of Helsinki Autocomplete API
  slug: university-of-helsinki-autocomplete-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Checklist API from University of Helsinki — 2 operation(s) for checklist.
  name: University of Helsinki Checklist API
  slug: university-of-helsinki-checklist-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Checklist Versions API from University of Helsinki — 2 operation(s) for checklist versions.
  name: University of Helsinki Checklist Versions API
  slug: university-of-helsinki-checklist-versions-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Collections API from University of Helsinki — 5 operation(s) for collections.
  name: University of Helsinki Collections API
  slug: university-of-helsinki-collections-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The CompanyContact API from University of Helsinki — 2 operation(s) for companycontact.
  name: University of Helsinki Company Contact API
  slug: university-of-helsinki-companycontact-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The CompanyOrganization API from University of Helsinki — 3 operation(s) for companyorganization.
  name: University of Helsinki Company Organization API
  slug: university-of-helsinki-companyorganization-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The CompanyTitle API from University of Helsinki — 1 operation(s) for companytitle.
  name: University of Helsinki Company Title API
  slug: university-of-helsinki-companytitle-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Contact API from University of Helsinki — 2 operation(s) for contact.
  name: University of Helsinki Contact API
  slug: university-of-helsinki-contact-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: Content type Course of type Content. Contains information related to a course, such as introduction text and an image.
  name: University of Helsinki Content - Course API
  slug: university-of-helsinki-content-course-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Coordinates API from University of Helsinki — 1 operation(s) for coordinates.
  name: University of Helsinki Coordinates API
  slug: university-of-helsinki-coordinates-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Documents API from University of Helsinki — 7 operation(s) for documents.
  name: University of Helsinki Documents API
  slug: university-of-helsinki-documents-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The /dynamicorder API from University of Helsinki — 8 operation(s) for /dynamicorder.
  name: University of Helsinki /dynamicorder API
  slug: university-of-helsinki-dynamicorder-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The EducationUnits API from University of Helsinki — 2 operation(s) for educationunits.
  name: University of Helsinki Education Units API
  slug: university-of-helsinki-educationunits-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Feedback API from University of Helsinki — 1 operation(s) for feedback.
  name: University of Helsinki Feedback API
  slug: university-of-helsinki-feedback-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The FieldOfScience API from University of Helsinki — 1 operation(s) for fieldofscience.
  name: University of Helsinki Field Of Science API
  slug: university-of-helsinki-fieldofscience-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Filter API from University of Helsinki — 2 operation(s) for filter.
  name: University of Helsinki Filter API
  slug: university-of-helsinki-filter-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The FinanceAndOldResearch API from University of Helsinki — 1 operation(s) for financeandoldresearch.
  name: University of Helsinki Finance And Old Research API
  slug: university-of-helsinki-financeandoldresearch-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The FinanceUnits API from University of Helsinki — 2 operation(s) for financeunits.
  name: University of Helsinki Finance Units API
  slug: university-of-helsinki-financeunits-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The FinanceUnitsPublic API from University of Helsinki — 1 operation(s) for financeunitspublic.
  name: University of Helsinki Finance Units Public API
  slug: university-of-helsinki-financeunitspublic-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The FinanceUnitsUniqueCode API from University of Helsinki — 1 operation(s) for financeunitsuniquecode.
  name: University of Helsinki Finance Units Unique Code API
  slug: university-of-helsinki-financeunitsuniquecode-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Form Permissions API from University of Helsinki — 3 operation(s) for form permissions.
  name: University of Helsinki Form Permissions API
  slug: university-of-helsinki-form-permissions-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Forms API from University of Helsinki — 4 operation(s) for forms.
  name: University of Helsinki Forms API
  slug: university-of-helsinki-forms-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The GeoConvert API from University of Helsinki — 6 operation(s) for geoconvert.
  name: University of Helsinki Geo Convert API
  slug: university-of-helsinki-geoconvert-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Google Maps API from University of Helsinki — 1 operation(s) for google maps.
  name: University of Helsinki Google Maps API
  slug: university-of-helsinki-google-maps-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Hosts API from University of Helsinki — 3 operation(s) for hosts.
  name: University of Helsinki Hosts API
  slug: university-of-helsinki-hosts-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The HrOrganization API from University of Helsinki — 3 operation(s) for hrorganization.
  name: University of Helsinki Hr Organization API
  slug: university-of-helsinki-hrorganization-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The HTML To PDF API from University of Helsinki — 1 operation(s) for html to pdf.
  name: University of Helsinki HTML To PDF API
  slug: university-of-helsinki-html-to-pdf-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The HumanResourcesAndResearchGroups API from University of Helsinki — 1 operation(s) for humanresourcesandresearchgroups.
  name: University of Helsinki Human Resources And Research Groups API
  slug: university-of-helsinki-humanresourcesandresearchgroups-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The HumanResourcesIamGroupPrefix API from University of Helsinki — 1 operation(s) for humanresourcesiamgroupprefix.
  name: University of Helsinki Human Resources Iam Group Prefix API
  slug: university-of-helsinki-humanresourcesiamgroupprefix-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The HumanResourcesSubunitToUnit API from University of Helsinki — 1 operation(s) for humanresourcessubunittounit.
  name: University of Helsinki Human Resources Subunit To Unit API
  slug: university-of-helsinki-humanresourcessubunittounit-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The HumanResourcesWithLevel API from University of Helsinki — 1 operation(s) for humanresourceswithlevel.
  name: University of Helsinki Human Resources With Level API
  slug: university-of-helsinki-humanresourceswithlevel-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Images API from University of Helsinki — 6 operation(s) for images.
  name: University of Helsinki Images API
  slug: university-of-helsinki-images-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Informal Taxon Groups API from University of Helsinki — 7 operation(s) for informal taxon groups.
  name: University of Helsinki Informal Taxon Groups API
  slug: university-of-helsinki-informal-taxon-groups-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Information API from University of Helsinki — 1 operation(s) for information.
  name: University of Helsinki Information API
  slug: university-of-helsinki-information-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The JSON-LD context API from University of Helsinki — 1 operation(s) for json-ld context.
  name: University of Helsinki JSON-LD context API
  slug: university-of-helsinki-json-ld-context-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Logger API from University of Helsinki — 2 operation(s) for logger.
  name: University of Helsinki Logger API
  slug: university-of-helsinki-logger-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Login API from University of Helsinki — 2 operation(s) for login.
  name: University of Helsinki Login API
  slug: university-of-helsinki-login-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The /machine API from University of Helsinki — 1 operation(s) for /machine.
  name: University of Helsinki /machine API
  slug: university-of-helsinki-machine-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Metadata API from University of Helsinki — 9 operation(s) for metadata.
  name: University of Helsinki Metadata API
  slug: university-of-helsinki-metadata-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Named places API from University of Helsinki — 3 operation(s) for named places.
  name: University of Helsinki Named places API
  slug: university-of-helsinki-named-places-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The News API from University of Helsinki — 4 operation(s) for news.
  name: University of Helsinki News API
  slug: university-of-helsinki-news-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The NodesInMultipleHierarchies API from University of Helsinki — 1 operation(s) for nodesinmultiplehierarchies.
  name: University of Helsinki Nodes In Multiple Hierarchies API
  slug: university-of-helsinki-nodesinmultiplehierarchies-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Notifications API from University of Helsinki — 2 operation(s) for notifications.
  name: University of Helsinki Notifications API
  slug: university-of-helsinki-notifications-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The OfficialUnits API from University of Helsinki — 2 operation(s) for officialunits.
  name: University of Helsinki Official Units API
  slug: university-of-helsinki-officialunits-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The /order API from University of Helsinki — 1 operation(s) for /order.
  name: University of Helsinki /order API
  slug: university-of-helsinki-order-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Organization API from University of Helsinki — 2 operation(s) for organization.
  name: University of Helsinki Organization API
  slug: university-of-helsinki-organization-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Organizations API from University of Helsinki — 2 operation(s) for organizations.
  name: University of Helsinki Organizations API
  slug: university-of-helsinki-organizations-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Person API from University of Helsinki — 6 operation(s) for person.
  name: University of Helsinki Person API
  slug: university-of-helsinki-person-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Publications API from University of Helsinki — 1 operation(s) for publications.
  name: University of Helsinki Publications API
  slug: university-of-helsinki-publications-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Red List Evaluation Groups API from University of Helsinki — 7 operation(s) for red list evaluation groups.
  name: University of Helsinki Red List Evaluation Groups API
  slug: university-of-helsinki-red-list-evaluation-groups-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The ResearchGroups API from University of Helsinki — 1 operation(s) for researchgroups.
  name: University of Helsinki Research Groups API
  slug: university-of-helsinki-researchgroups-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The ResearchOrganization API from University of Helsinki — 1 operation(s) for researchorganization.
  name: University of Helsinki Research Organization API
  slug: university-of-helsinki-researchorganization-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The ResearchResources API from University of Helsinki — 1 operation(s) for researchresources.
  name: University of Helsinki Research Resources API
  slug: university-of-helsinki-researchresources-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Shorthands API from University of Helsinki — 4 operation(s) for shorthands.
  name: University of Helsinki Shorthands API
  slug: university-of-helsinki-shorthands-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Sound identification API from University of Helsinki — 1 operation(s) for sound identification.
  name: University of Helsinki Sound identification API
  slug: university-of-helsinki-sound-identification-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Sources API from University of Helsinki — 2 operation(s) for sources.
  name: University of Helsinki Sources API
  slug: university-of-helsinki-sources-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The /ss API from University of Helsinki — 3 operation(s) for /ss.
  name: University of Helsinki /ss API
  slug: university-of-helsinki-ss-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The SteeringGroup API from University of Helsinki — 3 operation(s) for steeringgroup.
  name: University of Helsinki Steering Group API
  slug: university-of-helsinki-steeringgroup-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The SteeringGroups API from University of Helsinki — 1 operation(s) for steeringgroups.
  name: University of Helsinki Steering Groups API
  slug: university-of-helsinki-steeringgroups-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: Study search content. The API returns the study options and/or degree programmes content for University of Helsinki in an indexable format. The API strives to provide each content again if the content
  name: University of Helsinki Study Search API
  slug: university-of-helsinki-study-search-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Suggestion API from University of Helsinki — 1 operation(s) for suggestion.
  name: University of Helsinki Suggestion API
  slug: university-of-helsinki-suggestion-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Taxa API from University of Helsinki — 12 operation(s) for taxa.
  name: University of Helsinki Taxa API
  slug: university-of-helsinki-taxa-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The /ticket API from University of Helsinki — 1 operation(s) for /ticket.
  name: University of Helsinki /ticket API
  slug: university-of-helsinki-ticket-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Title API from University of Helsinki — 1 operation(s) for title.
  name: University of Helsinki Title API
  slug: university-of-helsinki-title-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Trait API from University of Helsinki — 32 operation(s) for trait.
  name: University of Helsinki Trait API
  slug: university-of-helsinki-trait-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The UniversityOfHelsinkiGroup API from University of Helsinki — 1 operation(s) for universityofhelsinkigroup.
  name: University of Helsinki University Of Helsinki Group API
  slug: university-of-helsinki-universityofhelsinkigroup-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The UniversityOfHelsinkiSubunitToUnit API from University of Helsinki — 1 operation(s) for universityofhelsinkisubunittounit.
  name: University of Helsinki University Of Helsinki Subunit To Unit API
  slug: university-of-helsinki-universityofhelsinkisubunittounit-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: Employee Information REST service
  name: University of Helsinki /v1 API
  slug: university-of-helsinki-v1-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: University buildings rest service
  name: University of Helsinki V1/building/ API
  slug: university-of-helsinki-v1-building-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: University spaces rest service
  name: University of Helsinki V1/space/ API
  slug: university-of-helsinki-v1-space-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Warehouse API from University of Helsinki — 23 operation(s) for warehouse.
  name: University of Helsinki Warehouse API
  slug: university-of-helsinki-warehouse-api
- baseURL: https://api.helsinki.fi/portal/environments/DEFAULT
  baseurl_source: declared
  description: The Human Resources API from University of Helsinki — 1 operation(s) for human resources.
  name: University of Helsinki Human Resources API
  slug: university-of-helsinki-human-resources-api
artifact_total: 114
common:
- group: company
  title: ''
  type: Website
  url: https://www.helsinki.fi/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.helsinki.fi/portal/
- group: docs
  title: ''
  type: APIReference
  url: https://api.helsinki.fi/portal/environments/DEFAULT/apis
- group: docs
  title: ''
  type: Documentation
  url: https://api.helsinki.fi/portal/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UniversityofHelsinki
- group: build
  title: ''
  type: GitHub
  url: https://github.com/UniversityofHelsinki
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/UH-StudentServices
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-helsinki/
- group: company
  title: ''
  type: Blog
  url: https://blogs.helsinki.fi/
- group: company
  title: ''
  type: News
  url: https://www.helsinki.fi/en/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.helsinki.fi/en/about-us/processing-data-university/data-protection
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.helsinki.fi/.well-known/security.txt
- group: other
  title: ''
  type: ResearchRepository
  url: https://helda.helsinki.fi/
- group: other
  title: ''
  type: OpenData
  url: https://datakatalogi.helsinki.fi/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://helka.helsinki.fi/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://studies.helsinki.fi/courses
- group: other
  title: ''
  type: IdentityFederation
  url: https://login.helsinki.fi/idp/shibboleth
- group: other
  title: ''
  type: IdentityFederation
  url: https://haka.funet.fi/metadata/haka-metadata.xml
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.helsinki.fi/en/research/research-units-and-infrastructures/research-infrastructures
- group: other
  title: ''
  type: AIPolicy
  url: https://studies.helsinki.fi/instructions/article/using-ai-support-learning
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/university-of-helsinki/refs/heads/main/openapi/university-of-helsinki-hy-organisation-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/university-of-helsinki-hy-organisation-api-openapi.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/university-of-helsinki/refs/heads/main/json-schema/university-of-helsinki-hy-organisation-api-schemas.json
  title: ''
  type: JSONSchema
  url: json-schema/university-of-helsinki-hy-organisation-api-schemas.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/university-of-helsinki/refs/heads/main/authentication/university-of-helsinki-authentication.yml
  title: ''
  type: Authentication
  url: authentication/university-of-helsinki-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/university-of-helsinki/refs/heads/main/scopes/university-of-helsinki-scopes.yml
  title: ''
  type: Scopes
  url: scopes/university-of-helsinki-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/university-of-helsinki/refs/heads/main/errors/university-of-helsinki-problem-types.yml
  title: ''
  type: Errors
  url: errors/university-of-helsinki-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/university-of-helsinki/refs/heads/main/conformance/university-of-helsinki-conformance.yml
  title: ''
  type: Conformance
  url: conformance/university-of-helsinki-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/university-of-helsinki/refs/heads/main/lifecycle/university-of-helsinki-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-helsinki-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/university-of-helsinki/refs/heads/main/vocabulary/university-of-helsinki-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-helsinki-vocabulary.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/university-of-helsinki/refs/heads/main/examples/university-of-helsinki-examples.yml
  title: ''
  type: Examples
  url: examples/university-of-helsinki-examples.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/university-of-helsinki/refs/heads/main/rules/university-of-helsinki-openapi-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/university-of-helsinki-openapi-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/university-of-helsinki/refs/heads/main/json-ld/university-of-helsinki-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/university-of-helsinki-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/university-of-helsinki/refs/heads/main/graphql/university-of-helsinki-graphql.md
  title: ''
  type: GraphQL
  url: graphql/university-of-helsinki-graphql.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/university-of-helsinki/refs/heads/main/well-known/university-of-helsinki-openid-configuration.json
  title: ''
  type: WellKnown
  url: well-known/university-of-helsinki-openid-configuration.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/university-of-helsinki/refs/heads/main/security/university-of-helsinki-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-helsinki-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/university-of-helsinki/refs/heads/main/security/university-of-helsinki-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/university-of-helsinki-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/university-of-helsinki/refs/heads/main/plans/university-of-helsinki-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/university-of-helsinki-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/university-of-helsinki/refs/heads/main/rate-limits/university-of-helsinki-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/university-of-helsinki-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/university-of-helsinki/refs/heads/main/finops/university-of-helsinki-finops.yml
  title: ''
  type: FinOps
  url: finops/university-of-helsinki-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/university-of-helsinki/refs/heads/main/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Helsinki is Finland''s oldest and largest multidisciplinary research university, founded in 1640, and it is one of the very few institutions in this cohort that operates a real, first-party API program rather than only renting vendor platforms. It runs its own Gravitee API gateway at gw.api.helsinki.fi behind a public developer portal at api.helsinki.fi, listing fifteen public APIs — organisations, buildings and spaces, employee and group directories, service management, the application-portfolio register, network registry, and the CMS behind helsinki.fi and the course pages — twelve of which publish a readable OpenAPI. Alongside that sit genuinely institution-operated scholarly and identity infrastructure: Helda (DSpace 7.6.2) and the newer HY Data Catalogue (DSpace 9.0), three live OAI-PMH endpoints, the Editori open-publishing service, the Shibboleth/OIDC identity provider at login.helsinki.fi with sixteen entities registered in the Haka federation, and
  the Finnish Biodiversity Information Facility (api.laji.fi, 177 paths), which is run by Luomus, a University institute. What the University does NOT author is equally important and is recorded here as tenancy rather than as its own work: Sisu/Kori is Funidata''s, the research portal is Elsevier Pure, and Helka is Ex Libris Primo. The gateway is affiliation-gated — keyless access is disabled and portal self-registration is off — so the catalogue and every specification are readable by anyone, while a credential requires a university or Haka identity.'
finops:
- name: University Of Helsinki Finops
  service_category: Education
  slug: university-of-helsinki-finops
graphqls:
- description: '<!-- x-method: searched -->'
  name: GraphQL at the University of Helsinki
  slug: university-of-helsinki-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-helsinki.png
json_schemas:
- name: University of Helsinki - Contact Search API — component schemas
  property_count: 0
  slug: university-of-helsinki-contact-search-api-schemas
- name: University of Helsinki - Courses content machine - JSON API — component schemas
  property_count: 0
  slug: university-of-helsinki-course-pages-cms-schemas
- name: EmployeeInformationAPI — component schemas
  property_count: 0
  slug: university-of-helsinki-employeeinformationapi-schemas
- name: Laji API — component schemas
  property_count: 0
  slug: university-of-helsinki-finbif-laji-schemas
- name: General Efecte API — component schemas
  property_count: 0
  slug: university-of-helsinki-general-efecte-api-schemas
- name: Helsinki.fi content — component schemas
  property_count: 0
  slug: university-of-helsinki-helsinki-fi-content-schemas
- name: HY Building API — component schemas
  property_count: 0
  slug: university-of-helsinki-hy-building-api-schemas
- name: Organisation Registry Public API — component schemas
  property_count: 0
  slug: university-of-helsinki-hy-organisation-api-schemas
- name: network registry — component schemas
  property_count: 0
  slug: university-of-helsinki-network-registry-api-schemas
- name: HY Person/Group API — component schemas
  property_count: 0
  slug: university-of-helsinki-persongroup-schemas
- name: ServiceAPI — component schemas
  property_count: 0
  slug: university-of-helsinki-serviceapi-schemas
jsonld:
- class_count: 30
  name: University Of Helsinki Context
  property_count: 5
  slug: university-of-helsinki-context
layout: provider
modified: '2026-08-30'
name: University of Helsinki
nav: Providers
network: true
overview: 'University of Helsinki publishes 80 APIs on the [APIs.io](https://apis.io/) network, including All Node Attributes API, All Successors And Predecessors API, Annotations API, and 77 more. Tagged areas include Education, Higher Education, University, Finland, and Nordic.


  The University of Helsinki catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Helsinki''s developer surface includes API reference, documentation, GitHub presence, engineering blog, product news, authentication, code examples, and 32 more developer resources.'
plans:
- name: University Of Helsinki Plans Pricing
  plan_count: 3
  slug: university-of-helsinki-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: University Of Helsinki Rate Limits
  slug: university-of-helsinki-rate-limits
rules:
- effective_rule_count: 13
  extends: []
  name: University of Helsinki API Rules
  rule_count: 13
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 8
  slug: university-of-helsinki-openapi-spectral-rules
scopes:
- name: University Of Helsinki Scopes
  scope_count: 0
  slug: university-of-helsinki-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 50.0
    contract_governance: 29.5
    contract_quality: 69.2
    developer_ergonomics: 40.5
    discoverability: 70.4
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - finland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 54.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 80
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 83.3
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-helsinki/refs/heads/main/screenshots/university-of-helsinki-2026-06-20T200155.png
security:
- kind: authentication
  name: University Of Helsinki Authentication
  slug: university-of-helsinki-authentication
  summary_line: apiKey/http-bearer/oauth2 · 5 schemes
- kind: domain-security
  name: University Of Helsinki Domain Security
  slug: university-of-helsinki-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: University Of Helsinki Vulnerability Disclosure
  slug: university-of-helsinki-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: university-of-helsinki
tags:
- Education
- Higher Education
- University
- Finland
- Nordic
- Research
- Open Data
- Research Data
- Institutional Repository
- OAI-PMH
- Identity Federation
- API Gateway
- Course Catalog
- Library
- Biodiversity
website: https://www.helsinki.fi/en
---

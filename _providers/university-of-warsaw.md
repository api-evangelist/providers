---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 473
  human_in_the_loop: 12
  name: University Of Warsaw Agentic Access
  operation_count: 1076
  slug: university-of-warsaw-agentic-access
  summary_line: 1076 operations · 473 acting · 12 human-in-the-loop
api_count: 3
apis:
- description: 'The University of Warsaw Research Data Repository (Dane Badawcze UW) is a Dataverse-based institutional repository for long-term storage and open sharing of research data across all disciplines, with '
  name: Dane Badawcze UW Research Data Repository REST API
  slug: rdr-rest
- description: OAI-PMH 2.0 metadata harvesting endpoint for the University of Warsaw Research Data Repository (Dataverse). The repository identifies itself as the "Dane Badawcze UW Dataverse OAI Archive" and support
  name: Dane Badawcze UW OAI-PMH Endpoint
  slug: rdr-oai-pmh
- baseURL: https://usosapps.uw.edu.pl/services/
  baseurl_source: declared
  description: Machine-readable method reference
  name: University of Warsaw apiref API
  slug: university-of-warsaw-apiref-api
- baseURL: https://usosapps.uw.edu.pl/services/
  baseurl_source: declared
  description: USOS API server information and time
  name: University of Warsaw apisrv API
  slug: university-of-warsaw-apisrv-api
- baseURL: https://usosapps.uw.edu.pl/services/
  baseurl_source: declared
  description: Academic calendar events
  name: University of Warsaw calendar API
  slug: university-of-warsaw-calendar-api
- baseURL: https://usosapps.uw.edu.pl/services/
  baseurl_source: declared
  description: Courses and course editions
  name: University of Warsaw courses API
  slug: university-of-warsaw-courses-api
- baseURL: https://usosapps.uw.edu.pl/services/
  baseurl_source: declared
  description: Faculties and organizational units
  name: University of Warsaw fac API
  slug: university-of-warsaw-fac-api
- description: The Institutional Repository of the University of Warsaw (ReIn UW, Repozytorium Instytucjonalne Uniwersytetu Warszawskiego) runs DSpace-CRIS 8.1 (cris-2024.02.01) on the university's own host and expo
  name: ReIn UW Institutional Repository REST API
  slug: rein-uw-rest
- description: OAI-PMH 2.0 metadata harvesting endpoint for the Institutional Repository of the University of Warsaw. verb=Identify returns repositoryName "The Institutional Repository of the University of Warsaw (R
  name: ReIn UW OAI-PMH Endpoint
  slug: rein-uw-oai-pmh
- description: The university's own Shibboleth SAML 2.0 identity provider, entityID https://login.uw.edu.pl/idp, fronted by an Apereo CAS login at logowanie.uw.edu.pl. Its metadata is machine-readable at the entityI
  name: University of Warsaw SAML Identity Provider (eduGAIN / PIONIER.Id)
  slug: saml-idp
- description: 'The University of Warsaw registers DOIs through DataCite. Its DataCite provider is `repod` — "University of Warsaw – Interdisciplinary Centre for Mathematical and Computational Modelling", memberType '
  name: DataCite DOI Registration (REPOD / REPOD.DBUW)
  slug: datacite-membership
- description: The University of Warsaw is Crossref member 4211, holding 31 DOI prefixes used across its journals and press imprints (10.7311, 10.14394, 10.7172, 10.55226, 10.67180 and others). The membership is a f
  name: Crossref Membership (member 4211)
  slug: crossref-membership
- description: The Research Organization Registry record for the University of Warsaw, https://ror.org/039bjqg32, resolvable through the ROR API. It is the identifier the DataCite provider record for the university'
  name: ROR Registration (039bjqg32)
  slug: ror-registration
- description: The University of Warsaw Library (BUW) migrated off NUKAT to Ex Libris Alma with Primo discovery in December 2024, joining the national OMNIS shared catalogue. The discovery view is the institution-sp
  name: BUW Library Discovery (Ex Libris Alma / Primo, OMNIS)
  slug: buw-primo
- description: RepOD is Poland's general-purpose repository for open research data, running the same Dataverse build (1.3.2) as Dane Badawcze UW and operated by the Interdisciplinary Centre for Mathematical and Comp
  name: RepOD — Repository for Open Data (ICM UW)
  slug: repod
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The AchievementsSummary API from University of Warsaw — 2 operation(s) for achievementssummary.
  name: University of Warsaw Achievements Summary API
  slug: university-of-warsaw-achievementssummary-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Admin API from University of Warsaw — 9 operation(s) for admin.
  name: University of Warsaw Admin API
  slug: university-of-warsaw-admin-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Analysis API from University of Warsaw — 2 operation(s) for analysis.
  name: University of Warsaw Analysis API
  slug: university-of-warsaw-analysis-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ApiKeyPrincipal API from University of Warsaw — 3 operation(s) for apikeyprincipal.
  name: University of Warsaw API Key Principal API
  slug: university-of-warsaw-apikeyprincipal-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Article API from University of Warsaw — 3 operation(s) for article.
  name: University of Warsaw Article API
  slug: university-of-warsaw-article-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ArticleMyUw API from University of Warsaw — 2 operation(s) for articlemyuw.
  name: University of Warsaw Article My Uw API
  slug: university-of-warsaw-articlemyuw-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The AssetMigration API from University of Warsaw — 4 operation(s) for assetmigration.
  name: University of Warsaw Asset Migration API
  slug: university-of-warsaw-assetmigration-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Assets API from University of Warsaw — 5 operation(s) for assets.
  name: University of Warsaw Assets API
  slug: university-of-warsaw-assets-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Building API from University of Warsaw — 25 operation(s) for building.
  name: University of Warsaw Building API
  slug: university-of-warsaw-building-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The BuildingAccessibility API from University of Warsaw — 13 operation(s) for buildingaccessibility.
  name: University of Warsaw Building Accessibility API
  slug: university-of-warsaw-buildingaccessibility-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The BuildingAttribute API from University of Warsaw — 3 operation(s) for buildingattribute.
  name: University of Warsaw Building Attribute API
  slug: university-of-warsaw-buildingattribute-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The BuildingBon API from University of Warsaw — 7 operation(s) for buildingbon.
  name: University of Warsaw Building Bon API
  slug: university-of-warsaw-buildingbon-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The BuildingMigration API from University of Warsaw — 5 operation(s) for buildingmigration.
  name: University of Warsaw Building Migration API
  slug: university-of-warsaw-buildingmigration-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The BuildingMyUw API from University of Warsaw — 10 operation(s) for buildingmyuw.
  name: University of Warsaw Building My Uw API
  slug: university-of-warsaw-buildingmyuw-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The BuildingOkUw API from University of Warsaw — 11 operation(s) for buildingokuw.
  name: University of Warsaw Building Ok Uw API
  slug: university-of-warsaw-buildingokuw-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The BusinessEntity API from University of Warsaw — 3 operation(s) for businessentity.
  name: University of Warsaw Business Entity API
  slug: university-of-warsaw-businessentity-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The CalculatePermissions API from University of Warsaw — 4 operation(s) for calculatepermissions.
  name: University of Warsaw Calculate Permissions API
  slug: university-of-warsaw-calculatepermissions-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Campus API from University of Warsaw — 2 operation(s) for campus.
  name: University of Warsaw Campus API
  slug: university-of-warsaw-campus-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Country API from University of Warsaw — 1 operation(s) for country.
  name: University of Warsaw Country API
  slug: university-of-warsaw-country-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Course API from University of Warsaw — 27 operation(s) for course.
  name: University of Warsaw Course API
  slug: university-of-warsaw-course-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The CourseAdmin API from University of Warsaw — 16 operation(s) for courseadmin.
  name: University of Warsaw Course Admin API
  slug: university-of-warsaw-courseadmin-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The CourseAreasInterests API from University of Warsaw — 2 operation(s) for courseareasinterests.
  name: University of Warsaw Course Areas Interests API
  slug: university-of-warsaw-courseareasinterests-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The CourseCertificateAdmin API from University of Warsaw — 10 operation(s) for coursecertificateadmin.
  name: University of Warsaw Course Certificate Admin API
  slug: university-of-warsaw-coursecertificateadmin-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The CourseImportSp4eu/Export API from University of Warsaw — 6 operation(s) for courseimportsp4eu/export.
  name: University of Warsaw Course Import Sp4eu/Export API
  slug: university-of-warsaw-courseimportsp4eu-export-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The CourseMigration API from University of Warsaw — 7 operation(s) for coursemigration.
  name: University of Warsaw Course Migration API
  slug: university-of-warsaw-coursemigration-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The CourseMyUw API from University of Warsaw — 3 operation(s) for coursemyuw.
  name: University of Warsaw Course My Uw API
  slug: university-of-warsaw-coursemyuw-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The CourseRegistrationInfo API from University of Warsaw — 2 operation(s) for courseregistrationinfo.
  name: University of Warsaw Course Registration Info API
  slug: university-of-warsaw-courseregistrationinfo-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The CourseSp4eu API from University of Warsaw — 14 operation(s) for coursesp4eu.
  name: University of Warsaw Course Sp4eu API
  slug: university-of-warsaw-coursesp4eu-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The CpvCode API from University of Warsaw — 6 operation(s) for cpvcode.
  name: University of Warsaw Cpv Code API
  slug: university-of-warsaw-cpvcode-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Currency API from University of Warsaw — 2 operation(s) for currency.
  name: University of Warsaw Currency API
  slug: university-of-warsaw-currency-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Event API from University of Warsaw — 16 operation(s) for event.
  name: University of Warsaw Event API
  slug: university-of-warsaw-event-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The FAQ API from University of Warsaw — 2 operation(s) for faq.
  name: University of Warsaw FAQ API
  slug: university-of-warsaw-faq-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The FrameworkAgreement API from University of Warsaw — 20 operation(s) for frameworkagreement.
  name: University of Warsaw Framework Agreement API
  slug: university-of-warsaw-frameworkagreement-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The FrameworkAgreementMigration API from University of Warsaw — 4 operation(s) for frameworkagreementmigration.
  name: University of Warsaw Framework Agreement Migration API
  slug: university-of-warsaw-frameworkagreementmigration-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Giveaway API from University of Warsaw — 7 operation(s) for giveaway.
  name: University of Warsaw Giveaway API
  slug: university-of-warsaw-giveaway-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The GiveawayMyUw API from University of Warsaw — 3 operation(s) for giveawaymyuw.
  name: University of Warsaw Giveaway My Uw API
  slug: university-of-warsaw-giveawaymyuw-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The History API from University of Warsaw — 2 operation(s) for history.
  name: University of Warsaw History API
  slug: university-of-warsaw-history-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Home API from University of Warsaw — 3 operation(s) for home.
  name: University of Warsaw Home API
  slug: university-of-warsaw-home-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The HousingOption API from University of Warsaw — 6 operation(s) for housingoption.
  name: University of Warsaw Housing Option API
  slug: university-of-warsaw-housingoption-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The HousingOptions API from University of Warsaw — 8 operation(s) for housingoptions.
  name: University of Warsaw Housing Options API
  slug: university-of-warsaw-housingoptions-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The HousingOptionsSp4eu API from University of Warsaw — 6 operation(s) for housingoptionssp4eu.
  name: University of Warsaw Housing Options Sp4eu API
  slug: university-of-warsaw-housingoptionssp4eu-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The IdCard API from University of Warsaw — 4 operation(s) for idcard.
  name: University of Warsaw ID Card API
  slug: university-of-warsaw-idcard-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The IdCardMyUw API from University of Warsaw — 1 operation(s) for idcardmyuw.
  name: University of Warsaw ID Card My Uw API
  slug: university-of-warsaw-idcardmyuw-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The IdpPerson API from University of Warsaw — 3 operation(s) for idpperson.
  name: University of Warsaw Idp Person API
  slug: university-of-warsaw-idpperson-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ItemUsed API from University of Warsaw — 9 operation(s) for itemused.
  name: University of Warsaw Item Used API
  slug: university-of-warsaw-itemused-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ItemUsedMyUw API from University of Warsaw — 4 operation(s) for itemusedmyuw.
  name: University of Warsaw Item Used My Uw API
  slug: university-of-warsaw-itemusedmyuw-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ItService API from University of Warsaw — 8 operation(s) for itservice.
  name: University of Warsaw It Service API
  slug: university-of-warsaw-itservice-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ItServiceMyUw API from University of Warsaw — 2 operation(s) for itservicemyuw.
  name: University of Warsaw It Service My Uw API
  slug: university-of-warsaw-itservicemyuw-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Keywords API from University of Warsaw — 4 operation(s) for keywords.
  name: University of Warsaw Keywords API
  slug: university-of-warsaw-keywords-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Laboratory API from University of Warsaw — 12 operation(s) for laboratory.
  name: University of Warsaw Laboratory API
  slug: university-of-warsaw-laboratory-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The LaboratoryType API from University of Warsaw — 2 operation(s) for laboratorytype.
  name: University of Warsaw Laboratory Type API
  slug: university-of-warsaw-laboratorytype-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Language API from University of Warsaw — 1 operation(s) for language.
  name: University of Warsaw Language API
  slug: university-of-warsaw-language-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The License API from University of Warsaw — 6 operation(s) for license.
  name: University of Warsaw License API
  slug: university-of-warsaw-license-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The LicenseMigration API from University of Warsaw — 5 operation(s) for licensemigration.
  name: University of Warsaw License Migration API
  slug: university-of-warsaw-licensemigration-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Magazine API from University of Warsaw — 2 operation(s) for magazine.
  name: University of Warsaw Magazine API
  slug: university-of-warsaw-magazine-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The MagazineMigration API from University of Warsaw — 3 operation(s) for magazinemigration.
  name: University of Warsaw Magazine Migration API
  slug: university-of-warsaw-magazinemigration-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The MobilityOption API from University of Warsaw — 5 operation(s) for mobilityoption.
  name: University of Warsaw Mobility Option API
  slug: university-of-warsaw-mobilityoption-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The MobilityOptionAdmin API from University of Warsaw — 4 operation(s) for mobilityoptionadmin.
  name: University of Warsaw Mobility Option Admin API
  slug: university-of-warsaw-mobilityoptionadmin-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The MobilityOptionHome API from University of Warsaw — 3 operation(s) for mobilityoptionhome.
  name: University of Warsaw Mobility Option Home API
  slug: university-of-warsaw-mobilityoptionhome-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The MobilityOptionSp4eu API from University of Warsaw — 4 operation(s) for mobilityoptionsp4eu.
  name: University of Warsaw Mobility Option Sp4eu API
  slug: university-of-warsaw-mobilityoptionsp4eu-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The MonographPublisher API from University of Warsaw — 2 operation(s) for monographpublisher.
  name: University of Warsaw Monograph Publisher API
  slug: university-of-warsaw-monographpublisher-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The MonographPublisherMigration API from University of Warsaw — 3 operation(s) for monographpublishermigration.
  name: University of Warsaw Monograph Publisher Migration API
  slug: university-of-warsaw-monographpublishermigration-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PassControl API from University of Warsaw — 5 operation(s) for passcontrol.
  name: University of Warsaw Pass Control API
  slug: university-of-warsaw-passcontrol-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PassControlMigration API from University of Warsaw — 5 operation(s) for passcontrolmigration.
  name: University of Warsaw Pass Control Migration API
  slug: university-of-warsaw-passcontrolmigration-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PassControlMyUw API from University of Warsaw — 2 operation(s) for passcontrolmyuw.
  name: University of Warsaw Pass Control My Uw API
  slug: university-of-warsaw-passcontrolmyuw-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Patent API from University of Warsaw — 29 operation(s) for patent.
  name: University of Warsaw Patent API
  slug: university-of-warsaw-patent-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PatentPublic API from University of Warsaw — 1 operation(s) for patentpublic.
  name: University of Warsaw Patent Public API
  slug: university-of-warsaw-patentpublic-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PermDepartmentCasRole API from University of Warsaw — 2 operation(s) for permdepartmentcasrole.
  name: University of Warsaw Perm Department Cas Role API
  slug: university-of-warsaw-permdepartmentcasrole-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PermDepartmentPerson API from University of Warsaw — 4 operation(s) for permdepartmentperson.
  name: University of Warsaw Perm Department Person API
  slug: university-of-warsaw-permdepartmentperson-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Permissions API from University of Warsaw — 14 operation(s) for permissions.
  name: University of Warsaw Permissions API
  slug: university-of-warsaw-permissions-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PermsGroup API from University of Warsaw — 7 operation(s) for permsgroup.
  name: University of Warsaw Perms Group API
  slug: university-of-warsaw-permsgroup-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Person API from University of Warsaw — 3 operation(s) for person.
  name: University of Warsaw Person API
  slug: university-of-warsaw-person-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PersonAdmin API from University of Warsaw — 3 operation(s) for personadmin.
  name: University of Warsaw Person Admin API
  slug: university-of-warsaw-personadmin-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PersonDocument API from University of Warsaw — 3 operation(s) for persondocument.
  name: University of Warsaw Person Document API
  slug: university-of-warsaw-persondocument-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PersonPrincipal API from University of Warsaw — 8 operation(s) for personprincipal.
  name: University of Warsaw Person Principal API
  slug: university-of-warsaw-personprincipal-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PersonProfile API from University of Warsaw — 4 operation(s) for personprofile.
  name: University of Warsaw Person Profile API
  slug: university-of-warsaw-personprofile-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PersonRole API from University of Warsaw — 4 operation(s) for personrole.
  name: University of Warsaw Person Role API
  slug: university-of-warsaw-personrole-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PersonSystemRole API from University of Warsaw — 10 operation(s) for personsystemrole.
  name: University of Warsaw Person System Role API
  slug: university-of-warsaw-personsystemrole-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PersonSystemRoleDocsense API from University of Warsaw — 2 operation(s) for personsystemroledocsense.
  name: University of Warsaw Person System Role Docsense API
  slug: university-of-warsaw-personsystemroledocsense-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PersonSystemRoleMigration API from University of Warsaw — 5 operation(s) for personsystemrolemigration.
  name: University of Warsaw Person System Role Migration API
  slug: university-of-warsaw-personsystemrolemigration-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PersonSystemRoleSap API from University of Warsaw — 16 operation(s) for personsystemrolesap.
  name: University of Warsaw Person System Role Sap API
  slug: university-of-warsaw-personsystemrolesap-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PhoneNumber/Export API from University of Warsaw — 2 operation(s) for phonenumber/export.
  name: University of Warsaw Phone Number/Export API
  slug: university-of-warsaw-phonenumber-export-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Principal API from University of Warsaw — 3 operation(s) for principal.
  name: University of Warsaw Principal API
  slug: university-of-warsaw-principal-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Profile API from University of Warsaw — 32 operation(s) for profile.
  name: University of Warsaw Profile API
  slug: university-of-warsaw-profile-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ProfileDspace API from University of Warsaw — 3 operation(s) for profiledspace.
  name: University of Warsaw Profile Dspace API
  slug: university-of-warsaw-profiledspace-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ProfileMigration API from University of Warsaw — 11 operation(s) for profilemigration.
  name: University of Warsaw Profile Migration API
  slug: university-of-warsaw-profilemigration-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ProfileMyUw API from University of Warsaw — 7 operation(s) for profilemyuw.
  name: University of Warsaw Profile My Uw API
  slug: university-of-warsaw-profilemyuw-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ProfileOkUw API from University of Warsaw — 11 operation(s) for profileokuw.
  name: University of Warsaw Profile Ok Uw API
  slug: university-of-warsaw-profileokuw-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ProfilePerson API from University of Warsaw — 4 operation(s) for profileperson.
  name: University of Warsaw Profile Person API
  slug: university-of-warsaw-profileperson-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Project API from University of Warsaw — 26 operation(s) for project.
  name: University of Warsaw Project API
  slug: university-of-warsaw-project-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ProjectContractType API from University of Warsaw — 2 operation(s) for projectcontracttype.
  name: University of Warsaw Project Contract Type API
  slug: university-of-warsaw-projectcontracttype-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ProjectInternationalDetail API from University of Warsaw — 3 operation(s) for projectinternationaldetail.
  name: University of Warsaw Project International Detail API
  slug: university-of-warsaw-projectinternationaldetail-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ProjectMemberRole API from University of Warsaw — 5 operation(s) for projectmemberrole.
  name: University of Warsaw Project Member Role API
  slug: university-of-warsaw-projectmemberrole-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ProjectMigration API from University of Warsaw — 12 operation(s) for projectmigration.
  name: University of Warsaw Project Migration API
  slug: university-of-warsaw-projectmigration-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ProjectMyUw API from University of Warsaw — 5 operation(s) for projectmyuw.
  name: University of Warsaw Project My Uw API
  slug: university-of-warsaw-projectmyuw-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ProjectOkUw API from University of Warsaw — 3 operation(s) for projectokuw.
  name: University of Warsaw Project Ok Uw API
  slug: university-of-warsaw-projectokuw-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ProjectProgram API from University of Warsaw — 3 operation(s) for projectprogram.
  name: University of Warsaw Project Program API
  slug: university-of-warsaw-projectprogram-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ProjectProgramDetailed API from University of Warsaw — 3 operation(s) for projectprogramdetailed.
  name: University of Warsaw Project Program Detailed API
  slug: university-of-warsaw-projectprogramdetailed-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ProjectPublic API from University of Warsaw — 1 operation(s) for projectpublic.
  name: University of Warsaw Project Public API
  slug: university-of-warsaw-projectpublic-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ProjectReport API from University of Warsaw — 6 operation(s) for projectreport.
  name: University of Warsaw Project Report API
  slug: university-of-warsaw-projectreport-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PspElement API from University of Warsaw — 2 operation(s) for pspelement.
  name: University of Warsaw Psp Element API
  slug: university-of-warsaw-pspelement-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Publication API from University of Warsaw — 13 operation(s) for publication.
  name: University of Warsaw Publication API
  slug: university-of-warsaw-publication-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PublicationMigration API from University of Warsaw — 4 operation(s) for publicationmigration.
  name: University of Warsaw Publication Migration API
  slug: university-of-warsaw-publicationmigration-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PublicationMyUw API from University of Warsaw — 3 operation(s) for publicationmyuw.
  name: University of Warsaw Publication My Uw API
  slug: university-of-warsaw-publicationmyuw-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PublicProcurementLegalBasis API from University of Warsaw — 2 operation(s) for publicprocurementlegalbasis.
  name: University of Warsaw Public Procurement Legal Basis API
  slug: university-of-warsaw-publicprocurementlegalbasis-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PublicProcurementPlan API from University of Warsaw — 7 operation(s) for publicprocurementplan.
  name: University of Warsaw Public Procurement Plan API
  slug: university-of-warsaw-publicprocurementplan-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PublicProcurementPlanCategory API from University of Warsaw — 2 operation(s) for publicprocurementplancategory.
  name: University of Warsaw Public Procurement Plan Category API
  slug: university-of-warsaw-publicprocurementplancategory-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The PublicProcurementPlanMigration API from University of Warsaw — 5 operation(s) for publicprocurementplanmigration.
  name: University of Warsaw Public Procurement Plan Migration API
  slug: university-of-warsaw-publicprocurementplanmigration-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The RegistrationAdmin API from University of Warsaw — 3 operation(s) for registrationadmin.
  name: University of Warsaw Registration Admin API
  slug: university-of-warsaw-registrationadmin-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ResearchSet API from University of Warsaw — 7 operation(s) for researchset.
  name: University of Warsaw Research Set API
  slug: university-of-warsaw-researchset-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The SamlMetadata API from University of Warsaw — 2 operation(s) for samlmetadata.
  name: University of Warsaw Saml Metadata API
  slug: university-of-warsaw-samlmetadata-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The SapRole API from University of Warsaw — 2 operation(s) for saprole.
  name: University of Warsaw Sap Role API
  slug: university-of-warsaw-saprole-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The ScienceField/ScienceDiscipline API from University of Warsaw — 6 operation(s) for sciencefield/sciencediscipline.
  name: University of Warsaw Science Field/Science Discipline API
  slug: university-of-warsaw-sciencefield-sciencediscipline-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The StudentOrganization API from University of Warsaw — 16 operation(s) for studentorganization.
  name: University of Warsaw Student Organization API
  slug: university-of-warsaw-studentorganization-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The StudentOrganizationMyUw API from University of Warsaw — 2 operation(s) for studentorganizationmyuw.
  name: University of Warsaw Student Organization My Uw API
  slug: university-of-warsaw-studentorganizationmyuw-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The System API from University of Warsaw — 2 operation(s) for system.
  name: University of Warsaw System API
  slug: university-of-warsaw-system-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The system-rest API from University of Warsaw — 2 operation(s) for system-rest.
  name: University of Warsaw System Rest API
  slug: university-of-warsaw-system-rest-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The SystemRole API from University of Warsaw — 2 operation(s) for systemrole.
  name: University of Warsaw System Role API
  slug: university-of-warsaw-systemrole-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Translation API from University of Warsaw — 3 operation(s) for translation.
  name: University of Warsaw Translation API
  slug: university-of-warsaw-translation-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The TranslationCategory API from University of Warsaw — 2 operation(s) for translationcategory.
  name: University of Warsaw Translation Category API
  slug: university-of-warsaw-translationcategory-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The TranslationMigration API from University of Warsaw — 4 operation(s) for translationmigration.
  name: University of Warsaw Translation Migration API
  slug: university-of-warsaw-translationmigration-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Tutorial API from University of Warsaw — 6 operation(s) for tutorial.
  name: University of Warsaw Tutorial API
  slug: university-of-warsaw-tutorial-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The TutorialAdmin API from University of Warsaw — 3 operation(s) for tutorialadmin.
  name: University of Warsaw Tutorial Admin API
  slug: university-of-warsaw-tutorialadmin-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The TutorialMigration API from University of Warsaw — 4 operation(s) for tutorialmigration.
  name: University of Warsaw Tutorial Migration API
  slug: university-of-warsaw-tutorialmigration-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The TutorialSp4eu API from University of Warsaw — 4 operation(s) for tutorialsp4eu.
  name: University of Warsaw Tutorial Sp4eu API
  slug: university-of-warsaw-tutorialsp4eu-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Unit API from University of Warsaw — 8 operation(s) for unit.
  name: University of Warsaw Unit API
  slug: university-of-warsaw-unit-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The UniversityInfo API from University of Warsaw — 3 operation(s) for universityinfo.
  name: University of Warsaw University Info API
  slug: university-of-warsaw-universityinfo-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The UserPreference API from University of Warsaw — 1 operation(s) for userpreference.
  name: University of Warsaw User Preference API
  slug: university-of-warsaw-userpreference-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The UwEconomicDepartment API from University of Warsaw — 3 operation(s) for uweconomicdepartment.
  name: University of Warsaw Uw Economic Department API
  slug: university-of-warsaw-uweconomicdepartment-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The UwPerson API from University of Warsaw — 7 operation(s) for uwperson.
  name: University of Warsaw Uw Person API
  slug: university-of-warsaw-uwperson-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The UwPersonDocsense API from University of Warsaw — 3 operation(s) for uwpersondocsense.
  name: University of Warsaw Uw Person Docsense API
  slug: university-of-warsaw-uwpersondocsense-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The UwPersonMyUw API from University of Warsaw — 1 operation(s) for uwpersonmyuw.
  name: University of Warsaw Uw Person My Uw API
  slug: university-of-warsaw-uwpersonmyuw-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The UwUnit API from University of Warsaw — 6 operation(s) for uwunit.
  name: University of Warsaw Uw Unit API
  slug: university-of-warsaw-uwunit-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The UwUnitMyUw API from University of Warsaw — 2 operation(s) for uwunitmyuw.
  name: University of Warsaw Uw Unit My Uw API
  slug: university-of-warsaw-uwunitmyuw-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The API Key API from University of Warsaw — 3 operation(s) for api key.
  name: University of Warsaw API Key API
  slug: university-of-warsaw-api-key-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Phone Number API from University of Warsaw — 7 operation(s) for phone number.
  name: University of Warsaw Phone Number API
  slug: university-of-warsaw-phone-number-api
- baseURL: https://danebadawcze.uw.edu.pl/api/
  baseurl_source: declared
  description: The Project Type API from University of Warsaw — 3 operation(s) for project type.
  name: University of Warsaw Project Type API
  slug: university-of-warsaw-project-type-api
artifact_total: 178
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: USOS API (University of Warsaw) apiref API
  slug: open-university-of-warsaw-apiref-api
- collection_type: open
  name: USOS API (University of Warsaw) apiref apisrv API
  slug: open-university-of-warsaw-apisrv-api
- collection_type: open
  name: USOS API (University of Warsaw) apiref calendar API
  slug: open-university-of-warsaw-calendar-api
- collection_type: open
  name: USOS API (University of Warsaw) apiref courses API
  slug: open-university-of-warsaw-courses-api
- collection_type: open
  name: USOS API (University of Warsaw) apiref fac API
  slug: open-university-of-warsaw-fac-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/university-of-warsaw/refs/heads/main/capabilities/university-of-warsaw-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/university-of-warsaw-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/university-of-warsaw/refs/heads/main/agentic-access/university-of-warsaw-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-warsaw-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/university-of-warsaw/refs/heads/main/security/university-of-warsaw-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/university-of-warsaw-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/university-of-warsaw/refs/heads/main/authentication/university-of-warsaw-authentication.yml
  title: ''
  type: Authentication
  url: authentication/university-of-warsaw-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://en.uw.edu.pl/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/icm-uw
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/uniwersytet-warszawski
- group: start
  title: ''
  type: DeveloperPortal
  url: https://usosapps.uw.edu.pl/developers/
- group: auth
  title: ''
  type: Authentication
  url: https://usosapps.uw.edu.pl/developers/api/authorization/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/university-of-warsaw/refs/heads/main/plans/university-of-warsaw-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/university-of-warsaw-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/university-of-warsaw/refs/heads/main/rate-limits/university-of-warsaw-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/university-of-warsaw-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/university-of-warsaw/refs/heads/main/finops/university-of-warsaw-finops.yml
  title: ''
  type: FinOps
  url: finops/university-of-warsaw-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/university-of-warsaw/refs/heads/main/review.yml
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://en.uw.edu.pl/category/news/feed/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/university-of-warsaw/refs/heads/main/conformance/university-of-warsaw-conformance.yml
  title: ''
  type: Conformance
  url: conformance/university-of-warsaw-conformance.yml
- group: other
  title: ''
  type: ResearchRepository
  url: https://danebadawcze.uw.edu.pl/
- group: other
  title: ''
  type: ResearchRepository
  url: https://repozytorium.uw.edu.pl/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://omnis-buw.primo.exlibrisgroup.com/discovery/search?vid=48OMNIS_UOW:48UOW
- group: learn
  title: ''
  type: CourseCatalog
  url: https://usosapps.uw.edu.pl/developers/api/services/courses/
- group: other
  title: ''
  type: IdentityFederation
  url: https://login.uw.edu.pl/idp
- group: other
  title: ''
  type: ResearchComputing
  url: https://kdm.icm.edu.pl/
- group: other
  title: ''
  type: AIPolicy
  url: https://urk.uw.edu.pl/wytyczne_sztuczna_inteligencja/
- group: docs
  title: ''
  type: Documentation
  url: https://usosapps.uw.edu.pl/developers/api/
- group: docs
  title: ''
  type: APIReference
  url: https://api.sp4eu.uw.edu.pl/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uw.edu.pl/informacja-o-przetwarzaniu-danych-osobowych/
- group: operate
  title: ''
  type: Support
  url: https://it.uw.edu.pl/pl/
created: '2026-06-03'
description: 'The University of Warsaw (Uniwersytet Warszawski) is Poland''s largest and highest-ranked university and a member of the 4EU+ European University Alliance. Unusually for this cohort it operates real first-party programmable surfaces rather than only vendor tenancies: the USOS API at usosapps.uw.edu.pl, a documented OAuth 1.0a REST-like protocol over the institution''s own academic database (courses, faculties, calendar, users, payments), and two springdoc services that publish their own OpenAPI and Swagger UI — the Student Portal 4EU+ API at api.sp4eu.uw.edu.pl (OpenAPI 3.1, 74 paths, read endpoints answer anonymously) and Jaskier at api.jaskier.uw.edu.pl, the university''s central institutional API (OpenAPI 3.0.1, 729 paths, 458 schemas, bearer-gated data). Research data is handled by two institution-hosted repositories — Dane Badawcze UW (Dataverse, DOI prefix 10.58132) and ReIn UW (DSpace-CRIS 8.1) — each with a native REST API and an OAI-PMH 2.0 endpoint. The university
  runs its own Shibboleth SAML identity provider at login.uw.edu.pl, registered in eduGAIN through the Polish PIONIER.Id federation, and it is a DataCite repository client and a Crossref member with 31 DOI prefixes. What it does NOT have is a single central developer portal: the USOS developers site is the only signup surface, the library discovery layer is an Ex Libris Alma/Primo tenancy, and the LMS is a Moodle install with no public LTI advertisement.'
examples:
- key_count: 2
  name: University Of Warsaw Course Error Example
  slug: university-of-warsaw-course-error-example
- key_count: 6
  name: University Of Warsaw Installation Example
  slug: university-of-warsaw-installation-example
- key_count: 2
  name: University Of Warsaw Now Example
  slug: university-of-warsaw-now-example
- key_count: 3
  name: University Of Warsaw Sp4Eu Tutorial Example
  slug: university-of-warsaw-sp4eu-tutorial-example
finops:
- name: University Of Warsaw Finops
  service_category: Education
  slug: university-of-warsaw-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-warsaw.png
json_schemas:
- name: USOS Course
  property_count: 14
  slug: university-of-warsaw-course
- name: USOS Faculty
  property_count: 9
  slug: university-of-warsaw-faculty
- name: USOS Installation
  property_count: 9
  slug: university-of-warsaw-installation
- name: Student Portal 4EU+ Course
  property_count: 32
  slug: university-of-warsaw-sp4eu-course
- name: Student Portal 4EU+ Tutorial
  property_count: 16
  slug: university-of-warsaw-sp4eu-tutorial
json_structures:
- name: University Of Warsaw Course Structure
  property_count: 9
  slug: university-of-warsaw-course-structure
- name: University Of Warsaw Installation Structure
  property_count: 9
  slug: university-of-warsaw-installation-structure
jsonld:
- class_count: 23
  name: University Of Warsaw Context
  property_count: 8
  slug: university-of-warsaw-context
layout: provider
modified: '2026-09-01'
name: University of Warsaw
nav: Providers
network: true
overview: 'University of Warsaw publishes 142 APIs on the [APIs.io](https://apis.io/) network, including apiref API, apisrv API, calendar API, and 139 more. Tagged areas include Education, Higher Education, University, Poland, and Europe.


  The University of Warsaw catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Warsaw''s developer surface includes authentication, GitHub presence, engineering blog, documentation, API reference, support, and 20 more developer resources.'
plans:
- name: University Of Warsaw Plans Pricing
  plan_count: 2
  slug: university-of-warsaw-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: University Of Warsaw Rate Limits
  slug: university-of-warsaw-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of Warsaw API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: university-of-warsaw-jsonschema-spectral-rules
- effective_rule_count: 7
  extends: []
  name: University of Warsaw API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 4
  slug: university-of-warsaw-rules
score:
  band: developing
  composite: 53.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 77.3
    catalog_earned_first_party: 0.0
    catalog_gap: 37.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 52.6
    contract_governance: 14.4
    contract_quality: 65.5
    developer_ergonomics: 45.2
    discoverability: 68.5
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - poland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 52.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 142
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 53.7
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-warsaw/refs/heads/main/screenshots/university-of-warsaw-2026-06-20T200305.png
security:
- kind: authentication
  name: University Of Warsaw Authentication
  slug: university-of-warsaw-authentication
  summary_line: apiKey/oauth1a/bearer/saml · 4 schemes
- kind: domain-security
  name: University Of Warsaw Domain Security
  slug: university-of-warsaw-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: university-of-warsaw
tags:
- Education
- Higher Education
- University
- Poland
- Europe
- 4EU+ Alliance
- Academic Data
- Course Catalog
- Research Data
- Research Repository
- Identity Federation
- Library
- Open Data
website: https://en.uw.edu.pl/
---

---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Companies House Agentic Access
  operation_count: 28
  slug: companies-house-agentic-access
  summary_line: 28 operations
api_count: 9
apis:
- description: The Companies House Streaming API delivers real-time changes to Companies House data via long-running HTTP connections. It streams updates across nine data categories including company information, fi
  name: Companies House Streaming API
  slug: companies-house-streaming-api
- description: Charges
  name: Companies House charges API
  slug: companies-house-charges-api
- description: Filing history
  name: Companies House filingHistory API
  slug: companies-house-filinghistory-api
- description: Insolvency
  name: Companies House insolvency API
  slug: companies-house-insolvency-api
- description: Officer disqualifications
  name: Companies House officerDisqualifications API
  slug: companies-house-officerdisqualifications-api
- description: Officers
  name: Companies House officers API
  slug: companies-house-officers-api
- description: Persons with significant control
  name: Companies House personsWithSignificantControl API
  slug: companies-house-personswithsignificantcontrol-api
- description: Registered office address
  name: Companies House registeredOfficeAddress API
  slug: companies-house-registeredofficeaddress-api
- description: Search
  name: Companies House search API
  slug: companies-house-search-api
artifact_total: 146
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/companies-house-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/companies-house-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/companies-house-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/companies-house-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.gov.uk/government/organisations/companies-house
- group: docs
  title: ''
  type: Documentation
  url: https://developer.company-information.service.gov.uk/overview
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/companieshouse
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/companies-house
- group: company
  title: ''
  type: Blog
  url: https://companieshouse.blog.gov.uk
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.company-information.service.gov.uk/overview
- group: operate
  title: ''
  type: StatusPage
  url: https://forum.companieshouse.gov.uk/c/api-changes/7
- group: other
  title: ''
  type: X
  url: https://x.com/CompaniesHouse
- group: operate
  title: ''
  type: Forums
  url: https://forum.companieshouse.gov.uk
- group: auth
  title: ''
  type: Authentication
  url: https://developer-specs.company-information.service.gov.uk/guides/authorisation
- group: commercial
  title: ''
  type: Plans
  url: plans/companies-house-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/companies-house-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/companies-house-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/companies-house-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/companies-house-context.jsonld
- group: company
  title: ''
  type: BlogRSS
  url: https://companieshouse.blog.gov.uk/feed/
- group: start
  title: ''
  type: BlogIndex
  url: blogs/blogs.json
created: '2026-06-12'
description: Companies House is the UK government executive agency and trading fund responsible for incorporating and dissolving limited companies and registering company information in Great Britain. The Companies House REST API provides a free, open, and standardised way to search and retrieve company registration data, including company profiles, officer appointments, persons of significant control, filing history, charges, and insolvency records. Developers can also access a real-time Streaming API that delivers changes to Companies House data as they happen, enabling applications to stay up-to-date without polling. Authentication is handled via API key using HTTP Basic Auth, and all access is provided free of charge with a generous rate limit.
examples:
- key_count: 28
  name: Companies House Examples
  slug: companies-house-examples
finops:
- name: Companies House Finops
  service_category: ''
  slug: companies-house-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/companies-house.png
json_schemas:
- name: accountInformation
  property_count: 3
  slug: accountinformation
- name: accountingReferenceDate
  property_count: 2
  slug: accountingreferencedate
- name: accountPeriodFrom
  property_count: 2
  slug: accountperiodfrom
- name: accountPeriodTo
  property_count: 2
  slug: accountperiodto
- name: accountsInformation
  property_count: 6
  slug: accountsinformation
- name: accountsRequired
  property_count: 2
  slug: accountsrequired
- name: address
  property_count: 9
  slug: address
- name: Registered Office Address
  property_count: 6
  slug: advanced_company_registered_office_address
- name: advanced_top_hit
  property_count: 0
  slug: advanced_top_hit
- name: advancedCompany
  property_count: 11
  slug: advancedcompany
- name: A list of companies
  property_count: 0
  slug: advancedcompanysearch
- name: alphabetical_top_hit
  property_count: 0
  slug: alphabetical_top_hit
- name: Alphabetical company
  property_count: 7
  slug: alphabeticalcompany
- name: List of companies
  property_count: 0
  slug: alphabeticalcompanysearch
- name: alterationsDesc
  property_count: 3
  slug: alterationsdesc
- name: annotation
  property_count: 3
  slug: annotation
- name: annualReturnInformation
  property_count: 4
  slug: annualreturninformation
- name: appointedTo
  property_count: 3
  slug: appointedto
- name: appointmentLinkTypes
  property_count: 1
  slug: appointmentlinktypes
- name: appointmentList
  property_count: 10
  slug: appointmentlist
- name: associatedFiling
  property_count: 3
  slug: associatedfiling
- name: branchCompanyDetails
  property_count: 3
  slug: branchcompanydetails
- name: case
  property_count: 6
  slug: case
- name: caseDates
  property_count: 2
  slug: casedates
- name: charge_links
  property_count: 1
  slug: charge_links
- name: chargeDetails
  property_count: 21
  slug: chargedetails
- name: chargeList
  property_count: 6
  slug: chargelist
- name: classificationDesc
  property_count: 2
  slug: classificationdesc
- name: CommonSearch
  property_count: 4
  slug: commonsearch
- name: CommonSearchItems
  property_count: 6
  slug: commonsearchitems
- name: companyDetails
  property_count: 5
  slug: companydetails
- name: companyExemptions
  property_count: 4
  slug: companyexemptions
- name: companyInsolvency
  property_count: 3
  slug: companyinsolvency
- name: companyProfile
  property_count: 32
  slug: companyprofile
- name: companyRegister
  property_count: 5
  slug: companyregister
- name: CompanySearch
  property_count: 2
  slug: companysearch
- name: CompanySearchItems
  property_count: 8
  slug: companysearchitems
- name: companyUKEstablishments
  property_count: 4
  slug: companyukestablishments
- name: confirmationOfStatementInformation
  property_count: 4
  slug: confirmationofstatementinformation
- name: contactDetails
  property_count: 1
  slug: contactdetails
- name: corporateAnnotation
  property_count: 3
  slug: corporateannotation
- name: corporateDisqualification
  property_count: 9
  slug: corporatedisqualification
- name: corporateIdent
  property_count: 5
  slug: corporateident
- name: dateOfBirth
  property_count: 2
  slug: dateofbirth
- name: diclosureTransparencyRulesChapterFiveAppliesItem
  property_count: 2
  slug: diclosuretransparencyruleschapterfiveappliesitem
- name: disqualification
  property_count: 11
  slug: disqualification
- name: DisqualifiedOfficerAddress
  property_count: 7
  slug: disqualifiedofficeraddress
- name: DisqualifiedOfficerSearch
  property_count: 2
  slug: disqualifiedofficersearch
- name: DisqualifiedOfficerSearchItems
  property_count: 4
  slug: disqualifiedofficersearchitems
- name: Registered Office Address
  property_count: 4
  slug: dissolved_company_registered_office_address
- name: dissolved_top_hit
  property_count: 0
  slug: dissolved_top_hit
- name: Dissolved company
  property_count: 10
  slug: dissolvedcompany
- name: List of dissolved companies
  property_count: 0
  slug: dissolvedcompanysearch
- name: exemptionItem
  property_count: 2
  slug: exemptionitem
- name: exemptions
  property_count: 5
  slug: exemptions
- name: fileWithin
  property_count: 1
  slug: filewithin
- name: filingHistoryItem
  property_count: 13
  slug: filinghistoryitem
- name: filingHistoryItemLinks
  property_count: 2
  slug: filinghistoryitemlinks
- name: filingHistoryList
  property_count: 7
  slug: filinghistorylist
- name: foreignCompanyDetails
  property_count: 8
  slug: foreigncompanydetails
- name: formerNames
  property_count: 2
  slug: formernames
- name: insolvency_case_links
  property_count: 1
  slug: insolvency_case_links
- name: insolvency_cases
  property_count: 2
  slug: insolvency_cases
- name: itemLinkTypes
  property_count: 2
  slug: itemlinktypes
- name: last_variation
  property_count: 3
  slug: last_variation
- name: lastAccounts
  property_count: 4
  slug: lastaccounts
- name: links
  property_count: 1
  slug: links
- name: linksDirectorsRegister
  property_count: 1
  slug: linksdirectorsregister
- name: linksItems
  property_count: 1
  slug: linksitems
- name: linksListLLPMembers
  property_count: 1
  slug: linkslistllpmembers
- name: linksListLLPUsualResidentialAddress
  property_count: 1
  slug: linkslistllpusualresidentialaddress
- name: linksListMembers
  property_count: 1
  slug: linkslistmembers
- name: linksListUsualResidentialAddress
  property_count: 1
  slug: linkslistusualresidentialaddress
- name: LinksModel
  property_count: 1
  slug: linksmodel
- name: linksPersonsWithSignificantControlRegister
  property_count: 1
  slug: linkspersonswithsignificantcontrolregister
- name: linksSecretaryRegister
  property_count: 1
  slug: linkssecretaryregister
- name: linksType
  property_count: 11
  slug: linkstype
- name: linkTypes
  property_count: 1
  slug: linktypes
- name: MatchesModel
  property_count: 3
  slug: matchesmodel
- name: nameElements
  property_count: 5
  slug: nameelements
- name: naturalDisqualification
  property_count: 13
  slug: naturaldisqualification
- name: nextAccounts
  property_count: 4
  slug: nextaccounts
- name: notificationList
  property_count: 11
  slug: notificationlist
- name: OfficerAddress
  property_count: 9
  slug: officeraddress
- name: officerAppointmentSummary
  property_count: 19
  slug: officerappointmentsummary
- name: OfficerDateOfBirth
  property_count: 2
  slug: officerdateofbirth
- name: officerLinkTypes
  property_count: 1
  slug: officerlinktypes
- name: officerList
  property_count: 9
  slug: officerlist
- name: OfficerSearch
  property_count: 2
  slug: officersearch
- name: OfficerSearchItems
  property_count: 5
  slug: officersearchitems
- name: officerSummary
  property_count: 20
  slug: officersummary
- name: originatingRegistry
  property_count: 2
  slug: originatingregistry
- name: particularDesc
  property_count: 7
  slug: particulardesc
- name: permission_to_act
  property_count: 4
  slug: permission_to_act
- name: persons_entitled
  property_count: 1
  slug: persons_entitled
- name: PersonswithsignificantcontrolAddress
  property_count: 9
  slug: personswithsignificantcontroladdress
- name: PersonswithsignificantcontrolDateOfBirth
  property_count: 2
  slug: personswithsignificantcontroldateofbirth
- name: PersonswithsignificantcontrolSearch
  property_count: 2
  slug: personswithsignificantcontrolsearch
- name: PersonswithsignificantcontrolSearchItems
  property_count: 5
  slug: personswithsignificantcontrolsearchitems
- name: practitionerAddress
  property_count: 6
  slug: practitioneraddress
- name: practitioners
  property_count: 5
  slug: practitioners
- name: Previous company name
  property_count: 4
  slug: previous_company_name
- name: previousCompanyNames
  property_count: 3
  slug: previouscompanynames
- name: principalOfficeAddress
  property_count: 9
  slug: principalofficeaddress
- name: pscExemptAsSharesAdmittedOnMarketItem
  property_count: 2
  slug: pscexemptassharesadmittedonmarketitem
- name: pscExemptAsTradingOnEuRegualatedMarketItem
  property_count: 2
  slug: pscexemptastradingoneuregualatedmarketitem
- name: pscExemptAsTradingOnRegulatedMarketItem
  property_count: 2
  slug: pscexemptastradingonregulatedmarketitem
- name: pscExemptAsTradingOnUkRegualatedMarketItem
  property_count: 2
  slug: pscexemptastradingonukregualatedmarketitem
- name: reason
  property_count: 4
  slug: reason
- name: registeredItems
  property_count: 3
  slug: registereditems
- name: registeredOfficeAddress
  property_count: 9
  slug: registeredofficeaddress
- name: registerListDirectors
  property_count: 3
  slug: registerlistdirectors
- name: registerListLLPMembers
  property_count: 3
  slug: registerlistllpmembers
- name: registerListLLPUsualResidentialAddress
  property_count: 3
  slug: registerlistllpusualresidentialaddress
- name: registerListMembers
  property_count: 3
  slug: registerlistmembers
- name: registerListPersonsWithSignificantControl
  property_count: 3
  slug: registerlistpersonswithsignificantcontrol
- name: registerListSecretaries
  property_count: 3
  slug: registerlistsecretaries
- name: registerListUsualResidentialAddress
  property_count: 3
  slug: registerlistusualresidentialaddress
- name: registers
  property_count: 7
  slug: registers
- name: resolution
  property_count: 6
  slug: resolution
- name: Search
  property_count: 2
  slug: search
- name: SearchItems
  property_count: 3
  slug: searchitems
- name: securedDetailsDesc
  property_count: 2
  slug: secureddetailsdesc
- name: self_links
  property_count: 1
  slug: self_links
- name: serviceAddress
  property_count: 8
  slug: serviceaddress
- name: transaction_links
  property_count: 2
  slug: transaction_links
- name: transactions
  property_count: 4
  slug: transactions
jsonld:
- class_count: 0
  name: Companies House Context
  property_count: 60
  slug: companies-house-context
layout: provider
modified: '2026-06-12'
name: Companies House
nav: Providers
network: true
overview: 'Companies House publishes 8 APIs on the [APIs.io](https://apis.io/) network, including charges API, filingHistory API, insolvency API, and 5 more. Tagged areas include Companies, UK Government, Business Registration, Company Search, and Officers.


  The Companies House catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Companies House''s developer surface includes authentication, documentation, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Companies House Plans Pricing
  plan_count: 2
  slug: companies-house-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Companies House Rate Limits
  slug: companies-house-rate-limits
rules:
- name: Companies House API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: companies-house-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.0
  delta: -4.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.0
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 50.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 42.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/companies-house/refs/heads/main/screenshots/companies-house-2026-06-20T174828.png
security:
- kind: authentication
  name: Companies House Authentication
  slug: companies-house-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Companies House Domain Security
  slug: companies-house-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Companies House Vulnerability Disclosure
  slug: companies-house-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: companies-house
tags:
- Companies
- UK Government
- Business Registration
- Company Search
- Officers
- Filing History
- Insolvency
- Charges
- Persons of Significant Control
- Open Data
website: https://www.gov.uk/government/organisations/companies-house
---

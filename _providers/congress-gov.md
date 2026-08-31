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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Congress Gov Agentic Access
  operation_count: 108
  slug: congress-gov-agentic-access
  summary_line: 108 operations
api_count: 1
apis:
- description: Returns amendment data from the API
  name: Congress.gov API amendments API
  slug: congress-gov-amendments-api
- description: Returns bill data from the API
  name: Congress.gov API bill API
  slug: congress-gov-bill-api
- description: Returns bound Congressional Record data from the API
  name: Congress.gov API bound-congressional-record API
  slug: congress-gov-bound-congressional-record-api
- description: Returns committee data from the API
  name: Congress.gov API committee API
  slug: congress-gov-committee-api
- description: Returns committee meeting data from the API
  name: Congress.gov API committee-meeting API
  slug: congress-gov-committee-meeting-api
- description: Returns committee print data from the API
  name: Congress.gov API committee-print API
  slug: congress-gov-committee-print-api
- description: Returns committee report data from the API
  name: Congress.gov API committee-report API
  slug: congress-gov-committee-report-api
- description: Returns congress and congressional sessions data from the API
  name: Congress.gov API congress API
  slug: congress-gov-congress-api
- description: Returns Congressional Record data from the API
  name: Congress.gov API congressional-record API
  slug: congress-gov-congressional-record-api
- description: Returns Congressional Research Service (CRS) report data from the API
  name: Congress.gov API crsreport API
  slug: congress-gov-crsreport-api
- description: Returns daily Congressional Record data from the API
  name: Congress.gov API daily-congressional-record API
  slug: congress-gov-daily-congressional-record-api
- description: Returns hearing data from the API
  name: Congress.gov API hearing API
  slug: congress-gov-hearing-api
- description: Returns House communication data from the API
  name: Congress.gov API house-communication API
  slug: congress-gov-house-communication-api
- description: Returns House requirement data from the API
  name: Congress.gov API house-requirement API
  slug: congress-gov-house-requirement-api
- description: '[BETA] Returns House of Representatives roll call vote data from the API'
  name: Congress.gov API house-vote API
  slug: congress-gov-house-vote-api
- description: Returns member data from the API
  name: Congress.gov API member API
  slug: congress-gov-member-api
- description: Returns nomination data from the API
  name: Congress.gov API nomination API
  slug: congress-gov-nomination-api
- description: Returns Senate communication data from the API
  name: Congress.gov API senate-communication API
  slug: congress-gov-senate-communication-api
- description: Returns summaries data from the API
  name: Congress.gov API summaries API
  slug: congress-gov-summaries-api
- description: Returns treaty data from the API
  name: Congress.gov API treaty API
  slug: congress-gov-treaty-api
artifact_total: 192
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Congress.gov amendments API
  slug: open-congress-gov-amendments-api
- collection_type: open
  name: Congress.gov amendments bill API
  slug: open-congress-gov-bill-api
- collection_type: open
  name: Congress.gov amendments bound-congressional-record API
  slug: open-congress-gov-bound-congressional-record-api
- collection_type: open
  name: Congress.gov amendments committee API
  slug: open-congress-gov-committee-api
- collection_type: open
  name: Congress.gov amendments committee-meeting API
  slug: open-congress-gov-committee-meeting-api
- collection_type: open
  name: Congress.gov amendments committee-print API
  slug: open-congress-gov-committee-print-api
- collection_type: open
  name: Congress.gov amendments committee-report API
  slug: open-congress-gov-committee-report-api
- collection_type: open
  name: .gov amendments congress API
  slug: open-congress-gov-congress-api
- collection_type: open
  name: Congress.gov amendments congressional-record API
  slug: open-congress-gov-congressional-record-api
- collection_type: open
  name: Congress.gov amendments crsreport API
  slug: open-congress-gov-crsreport-api
- collection_type: open
  name: Congress.gov amendments daily-congressional-record API
  slug: open-congress-gov-daily-congressional-record-api
- collection_type: open
  name: Congress.gov amendments hearing API
  slug: open-congress-gov-hearing-api
- collection_type: open
  name: Congress.gov amendments house-communication API
  slug: open-congress-gov-house-communication-api
- collection_type: open
  name: Congress.gov amendments house-requirement API
  slug: open-congress-gov-house-requirement-api
- collection_type: open
  name: Congress.gov amendments house-vote API
  slug: open-congress-gov-house-vote-api
- collection_type: open
  name: Congress.gov amendments member API
  slug: open-congress-gov-member-api
- collection_type: open
  name: Congress.gov amendments nomination API
  slug: open-congress-gov-nomination-api
- collection_type: open
  name: Congress.gov amendments senate-communication API
  slug: open-congress-gov-senate-communication-api
- collection_type: open
  name: Congress.gov amendments summaries API
  slug: open-congress-gov-summaries-api
- collection_type: open
  name: Congress.gov amendments treaty API
  slug: open-congress-gov-treaty-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/congress-gov-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/congress-gov-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/congress-gov-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/congress-gov-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.congress.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/LibraryOfCongress/api.congress.gov
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/LibraryOfCongress
- group: company
  title: ''
  type: Blog
  url: https://blogs.loc.gov/law/
- group: commercial
  title: ''
  type: Pricing
  url: https://api.congress.gov/sign-up/
- group: start
  title: ''
  type: Signup
  url: https://api.congress.gov/sign-up/
- group: build
  title: ''
  type: PostmanCollection
  url: https://documenter.getpostman.com/view/6803158/VV56LCkZ
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/LibraryOfCongress/api.congress.gov/blob/main/ChangeLog.md
- group: commercial
  title: ''
  type: Plans
  url: plans/congress-gov-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/congress-gov-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/congress-gov-finops.yml
created: '2026-06-13'
description: The official REST API for the United States Congress, provided by the Library of Congress. It offers public access to machine-readable legislative data including bills, amendments, laws, committee reports, the Congressional Record, nominations, treaties, CRS reports, house votes, hearings, and member information. The API is free to use and requires a key obtained via the Data.gov signup page. Responses are available in JSON or XML format, with version 3 (v3) as the current release.
examples:
- key_count: 3
  name: Congress Gov Amendment List Example
  slug: congress-gov-amendment-list-example
- key_count: 2
  name: Congress Gov Bill Detail Example
  slug: congress-gov-bill-detail-example
- key_count: 3
  name: Congress Gov Bill List Example
  slug: congress-gov-bill-list-example
- key_count: 3
  name: Congress Gov Committee List Example
  slug: congress-gov-committee-list-example
- key_count: 1
  name: Congress Gov Congressional Record Example
  slug: congress-gov-congressional-record-example
- key_count: 3
  name: Congress Gov Member List Example
  slug: congress-gov-member-list-example
- key_count: 3
  name: Congress Gov Nomination List Example
  slug: congress-gov-nomination-list-example
- key_count: 3
  name: Congress Gov Treaty List Example
  slug: congress-gov-treaty-list-example
finops:
- name: Congress Gov Finops
  service_category: ''
  slug: congress-gov-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/congress-gov.png
json_schemas:
- name: Actions
  property_count: 5
  slug: congress-gov-actions
- name: Activity
  property_count: 2
  slug: congress-gov-activity
- name: amendedBill
  property_count: 8
  slug: congress-gov-amendedbill
- name: Amendment
  property_count: 8
  slug: congress-gov-amendment
- name: AmendmentActions
  property_count: 0
  slug: congress-gov-amendmentactions
- name: AmendmentAmendments
  property_count: 0
  slug: congress-gov-amendmentamendments
- name: AmendmentCosponsors
  property_count: 0
  slug: congress-gov-amendmentcosponsors
- name: AmendmentNumber
  property_count: 10
  slug: congress-gov-amendmentnumber
- name: Amendments
  property_count: 7
  slug: congress-gov-amendments
- name: AmendmentText
  property_count: 0
  slug: congress-gov-amendmenttext
- name: article
  property_count: 2
  slug: congress-gov-article
- name: associatedBill
  property_count: 4
  slug: congress-gov-associatedbill
- name: associatedMeeting
  property_count: 2
  slug: congress-gov-associatedmeeting
- name: author
  property_count: 1
  slug: congress-gov-author
- name: Bill
  property_count: 10
  slug: congress-gov-bill
- name: BillDetail
  property_count: 12
  slug: congress-gov-billdetail
- name: BillSummaries
  property_count: 0
  slug: congress-gov-billsummaries
- name: billSummariesArray
  property_count: 5
  slug: congress-gov-billsummariesarray
- name: BoundCongressionalRecord
  property_count: 1
  slug: congress-gov-boundcongressionalrecord
- name: cboCost
  property_count: 4
  slug: congress-gov-cbocost
- name: Committee
  property_count: 6
  slug: congress-gov-committee
- name: committeeBill
  property_count: 7
  slug: congress-gov-committeebill
- name: CommitteeBills
  property_count: 3
  slug: congress-gov-committeebills
- name: CommitteeCommunication
  property_count: 5
  slug: congress-gov-committeecommunication
- name: CommitteeDetail
  property_count: 9
  slug: congress-gov-committeedetail
- name: committeeHistory
  property_count: 5
  slug: congress-gov-committeehistory
- name: CommitteeHouseCommunication
  property_count: 0
  slug: congress-gov-committeehousecommunication
- name: CommitteeMeeting
  property_count: 0
  slug: congress-gov-committeemeeting
- name: CommitteeMeetingDetail
  property_count: 16
  slug: congress-gov-committeemeetingdetail
- name: committeeMeetings
  property_count: 5
  slug: congress-gov-committeemeetings
- name: CommitteeNominations
  property_count: 0
  slug: congress-gov-committeenominations
- name: CommitteePrint
  property_count: 0
  slug: congress-gov-committeeprint
- name: committeePrintCommittees
  property_count: 3
  slug: congress-gov-committeeprintcommittees
- name: CommitteePrintDetail
  property_count: 10
  slug: congress-gov-committeeprintdetail
- name: CommitteePrintDetailText
  property_count: 0
  slug: congress-gov-committeeprintdetailtext
- name: committeePrints
  property_count: 5
  slug: congress-gov-committeeprints
- name: committeePrintText
  property_count: 2
  slug: congress-gov-committeeprinttext
- name: committeeReport
  property_count: 2
  slug: congress-gov-committeereport
- name: CommitteeReports
  property_count: 0
  slug: congress-gov-committeereports
- name: committeereportsformats
  property_count: 3
  slug: congress-gov-committeereportsformats
- name: CommitteeReportsNumber
  property_count: 0
  slug: congress-gov-committeereportsnumber
- name: CommitteeReportsText
  property_count: 0
  slug: congress-gov-committeereportstext
- name: Committees
  property_count: 8
  slug: congress-gov-committees
- name: CommitteeSenateCommunication
  property_count: 0
  slug: congress-gov-committeesenatecommunication
- name: communicationType
  property_count: 2
  slug: congress-gov-communicationtype
- name: Congress
  property_count: 4
  slug: congress-gov-congress
- name: Congresses
  property_count: 0
  slug: congress-gov-congresses
- name: CongressionalRecord
  property_count: 2
  slug: congress-gov-congressionalrecord
- name: CoSponsor
  property_count: 10
  slug: congress-gov-cosponsor
- name: CrsReport
  property_count: 1
  slug: congress-gov-crsreport
- name: CrsReportDetail
  property_count: 13
  slug: congress-gov-crsreportdetail
- name: DailyCongressionalRecord
  property_count: 0
  slug: congress-gov-dailycongressionalrecord
- name: DailyCongressionalRecordArticles
  property_count: 1
  slug: congress-gov-dailycongressionalrecordarticles
- name: DailyCongressionalRecordIssue
  property_count: 1
  slug: congress-gov-dailycongressionalrecordissue
- name: format
  property_count: 1
  slug: congress-gov-format
- name: formats
  property_count: 2
  slug: congress-gov-formats
- name: fullIssue
  property_count: 3
  slug: congress-gov-fullissue
- name: hearing
  property_count: 5
  slug: congress-gov-hearing
- name: HearingDetail
  property_count: 11
  slug: congress-gov-hearingdetail
- name: Hearings
  property_count: 0
  slug: congress-gov-hearings
- name: houseCommunication
  property_count: 6
  slug: congress-gov-housecommunication
- name: HouseCommunications
  property_count: 1
  slug: congress-gov-housecommunications
- name: HouseCommunicationTypeNumber
  property_count: 15
  slug: congress-gov-housecommunicationtypenumber
- name: HouseRequirement
  property_count: 1
  slug: congress-gov-houserequirement
- name: HouseRequirements
  property_count: 1
  slug: congress-gov-houserequirements
- name: HouseVote
  property_count: 13
  slug: congress-gov-housevote
- name: HouseVoteMembers
  property_count: 0
  slug: congress-gov-housevotemembers
- name: HouseVoteNumber
  property_count: 0
  slug: congress-gov-housevotenumber
- name: HouseVoteNumberBase
  property_count: 12
  slug: congress-gov-housevotenumberbase
- name: houseVoteResults
  property_count: 6
  slug: congress-gov-housevoteresults
- name: issues
  property_count: 7
  slug: congress-gov-issues
- name: latestAction
  property_count: 2
  slug: congress-gov-latestaction
- name: latestNominationAction
  property_count: 2
  slug: congress-gov-latestnominationaction
- name: Law
  property_count: 11
  slug: congress-gov-law
- name: LawNumber
  property_count: 23
  slug: congress-gov-lawnumber
- name: laws
  property_count: 2
  slug: congress-gov-laws
- name: leadership
  property_count: 2
  slug: congress-gov-leadership
- name: legislativeSubjects
  property_count: 2
  slug: congress-gov-legislativesubjects
- name: matchCommunication
  property_count: 2
  slug: congress-gov-matchcommunication
- name: MatchCommunications
  property_count: 1
  slug: congress-gov-matchcommunications
- name: meetingdocument
  property_count: 5
  slug: congress-gov-meetingdocument
- name: Member
  property_count: 15
  slug: congress-gov-member
- name: memberDetailTerms
  property_count: 7
  slug: congress-gov-memberdetailterms
- name: Members
  property_count: 8
  slug: congress-gov-members
- name: MemberSponsoredLegislation
  property_count: 0
  slug: congress-gov-membersponsoredlegislation
- name: memberTerms
  property_count: 2
  slug: congress-gov-memberterms
- name: Nomination
  property_count: 1
  slug: congress-gov-nomination
- name: NominationActions
  property_count: 1
  slug: congress-gov-nominationactions
- name: nominationCommittee
  property_count: 6
  slug: congress-gov-nominationcommittee
- name: NominationCommittees
  property_count: 1
  slug: congress-gov-nominationcommittees
- name: NominationHearing
  property_count: 1
  slug: congress-gov-nominationhearing
- name: NominationNominee
  property_count: 1
  slug: congress-gov-nominationnominee
- name: Nominations
  property_count: 1
  slug: congress-gov-nominations
- name: nominationType
  property_count: 2
  slug: congress-gov-nominationtype
- name: nominee
  property_count: 5
  slug: congress-gov-nominee
- name: nomineeAction
  property_count: 5
  slug: congress-gov-nomineeaction
- name: parentcommittee
  property_count: 3
  slug: congress-gov-parentcommittee
- name: party
  property_count: 2
  slug: congress-gov-party
- name: partyHistory
  property_count: 3
  slug: congress-gov-partyhistory
- name: policyArea
  property_count: 1
  slug: congress-gov-policyarea
- name: recordedVote
  property_count: 6
  slug: congress-gov-recordedvote
- name: RelatedBills
  property_count: 4
  slug: congress-gov-relatedbills
- name: relatedItem
  property_count: 3
  slug: congress-gov-relateditem
- name: relatedMaterial
  property_count: 5
  slug: congress-gov-relatedmaterial
- name: relationshipDetails
  property_count: 2
  slug: congress-gov-relationshipdetails
- name: sectionArticle
  property_count: 4
  slug: congress-gov-sectionarticle
- name: senatecommittee
  property_count: 3
  slug: congress-gov-senatecommittee
- name: senateCommunication
  property_count: 6
  slug: congress-gov-senatecommunication
- name: SenateCommunications
  property_count: 1
  slug: congress-gov-senatecommunications
- name: SenateCommunicationTypeNumber
  property_count: 8
  slug: congress-gov-senatecommunicationtypenumber
- name: Sessions
  property_count: 4
  slug: congress-gov-sessions
- name: sourceSystem
  property_count: 2
  slug: congress-gov-sourcesystem
- name: Sponsor
  property_count: 9
  slug: congress-gov-sponsor
- name: sponsoredLegislation
  property_count: 8
  slug: congress-gov-sponsoredlegislation
- name: subcommittees
  property_count: 3
  slug: congress-gov-subcommittees
- name: Subjects
  property_count: 2
  slug: congress-gov-subjects
- name: Summaries
  property_count: 0
  slug: congress-gov-summaries
- name: summariesArray
  property_count: 9
  slug: congress-gov-summariesarray
- name: summaryBill
  property_count: 8
  slug: congress-gov-summarybill
- name: Text
  property_count: 0
  slug: congress-gov-text
- name: textVersion
  property_count: 2
  slug: congress-gov-textversion
- name: textVersions
  property_count: 3
  slug: congress-gov-textversions
- name: Titles
  property_count: 0
  slug: congress-gov-titles
- name: titlesArray
  property_count: 6
  slug: congress-gov-titlesarray
- name: topic
  property_count: 1
  slug: congress-gov-topic
- name: Treaty
  property_count: 1
  slug: congress-gov-treaty
- name: treatyAction
  property_count: 5
  slug: congress-gov-treatyaction
- name: TreatyActions
  property_count: 1
  slug: congress-gov-treatyactions
- name: treatyCommittee
  property_count: 7
  slug: congress-gov-treatycommittee
- name: TreatyCommittees
  property_count: 1
  slug: congress-gov-treatycommittees
- name: TreatyDetail
  property_count: 1
  slug: congress-gov-treatydetail
- name: video
  property_count: 2
  slug: congress-gov-video
- name: voteParty
  property_count: 6
  slug: congress-gov-voteparty
- name: witness
  property_count: 3
  slug: congress-gov-witness
- name: witnessDocument
  property_count: 3
  slug: congress-gov-witnessdocument
jsonld:
- class_count: 0
  name: Congress Gov Context
  property_count: 89
  slug: congress-gov-context
layout: provider
modified: '2026-06-13'
name: Congress.gov API
nav: Providers
network: true
overview: 'Congress.gov API publishes 20 APIs on the [APIs.io](https://apis.io/) network, including amendments API, bill API, bound-congressional-record API, and 17 more. Tagged areas include Government, Legislative, Congress, Bills, and Amendments.


  The Congress.gov API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Congress.gov API''s developer surface includes authentication, documentation, engineering blog, pricing, signup flow, changelog, and 9 more developer resources.'
plans:
- name: Congress Gov Plans Pricing
  plan_count: 1
  slug: congress-gov-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Congress Gov Rate Limits
  slug: congress-gov-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Congress.gov API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: congress-gov-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 16
    catalog_gap: 43.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 9.8
    contract_quality: 52.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 52.6
  previous_composite: 46.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/congress-gov/refs/heads/main/screenshots/congress-gov-2026-06-20T174909.png
security:
- kind: authentication
  name: Congress Gov Authentication
  slug: congress-gov-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Congress Gov Domain Security
  slug: congress-gov-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: congress-gov
tags:
- Government
- Legislative
- Congress
- Bills
- Amendments
- Members
- Treaties
- Nominations
- Congressional Record
- US Federal
website: https://www.congress.gov/
---

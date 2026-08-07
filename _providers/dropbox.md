---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.3
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 231
  human_in_the_loop: 6
  name: Dropbox Agentic Access
  operation_count: 252
  slug: dropbox-agentic-access
  summary_line: 252 operations · 231 acting · 6 human-in-the-loop
api_count: 28
apis:
- description: The Account API from Dropbox — 4 operation(s) for account.
  name: Dropbox Account API
  slug: dropbox-account-api
- description: _md__OpenApi::TAG::API_APP::DESCRIPTION
  name: Dropbox Api App API
  slug: dropbox-api-app-api
- description: The Auth API from Dropbox — 2 operation(s) for auth.
  name: Dropbox Auth API
  slug: dropbox-auth-api
- description: _md__OpenApi::TAG::BULK_SEND_JOB::DESCRIPTION
  name: Dropbox Bulk Send Job API
  slug: dropbox-bulk-send-job-api
- description: The Check API from Dropbox — 2 operation(s) for check.
  name: Dropbox Check API
  slug: dropbox-check-api
- description: The Contacts API from Dropbox — 2 operation(s) for contacts.
  name: Dropbox Contacts API
  slug: dropbox-contacts-api
- description: _md__OpenApi::TAG::EMBEDDED::DESCRIPTION
  name: Dropbox Embedded API
  slug: dropbox-embedded-api
- description: 'This namespace contains helpers for property and template metadata endpoints. These endpoints enable you to tag arbitrary key/value data to Dropbox files. The most basic unit in this namespace is the '
  name: Dropbox File_properties API
  slug: dropbox-file-properties-api
- description: This namespace contains endpoints and data types for file request operations.
  name: Dropbox File_requests API
  slug: dropbox-file-requests-api
- description: This namespace contains endpoints and data types for basic file operations.
  name: Dropbox Files API
  slug: dropbox-files-api
- description: _md__OpenApi::TAG::OAUTH::DESCRIPTION
  name: Dropbox OAuth API
  slug: dropbox-oauth-api
- description: _md__OpenApi::TAG::REPORT::DESCRIPTION
  name: Dropbox Report API
  slug: dropbox-report-api
- description: This namespace contains endpoints and data types for creating and managing shared links and shared folders.
  name: Dropbox Sharing API
  slug: dropbox-sharing-api
- description: _md__OpenApi::TAG::SIGNATURE_REQUEST::DESCRIPTION
  name: Dropbox Signature Request API
  slug: dropbox-signature-request-api
- description: The Team API from Dropbox — 12 operation(s) for team.
  name: Dropbox Team API
  slug: dropbox-team-api
- description: The Team > Devices API from Dropbox — 4 operation(s) for team > devices.
  name: Dropbox Team > Devices API
  slug: dropbox-team-devices-api
- description: The Team > Groups API from Dropbox — 12 operation(s) for team > groups.
  name: Dropbox Team > Groups API
  slug: dropbox-team-groups-api
- description: The Team > Legal_holds API from Dropbox — 7 operation(s) for team > legal_holds.
  name: Dropbox Team > Legal_holds API
  slug: dropbox-team-legal-holds-api
- description: The Team > Linked_apps API from Dropbox — 4 operation(s) for team > linked_apps.
  name: Dropbox Team > Linked_apps API
  slug: dropbox-team-linked-apps-api
- description: The Team_log API from Dropbox — 2 operation(s) for team_log.
  name: Dropbox Team_log API
  slug: dropbox-team-log-api
- description: The Team > Member_space_limits API from Dropbox — 7 operation(s) for team > member_space_limits.
  name: Dropbox Team > Member_space_limits API
  slug: dropbox-team-member-space-limits-api
- description: The Team > Members API from Dropbox — 20 operation(s) for team > members.
  name: Dropbox Team > Members API
  slug: dropbox-team-members-api
- description: The Team > Namespaces API from Dropbox — 2 operation(s) for team > namespaces.
  name: Dropbox Team > Namespaces API
  slug: dropbox-team-namespaces-api
- description: The Team > Reports API from Dropbox — 4 operation(s) for team > reports.
  name: Dropbox Team > Reports API
  slug: dropbox-team-reports-api
- description: The Team > Team_folder API from Dropbox — 10 operation(s) for team > team_folder.
  name: Dropbox Team > Team_folder API
  slug: dropbox-team-team-folder-api
- description: _md__OpenApi::TAG::TEMPLATE::DESCRIPTION
  name: Dropbox Template API
  slug: dropbox-template-api
- description: _md__OpenApi::TAG::UNCLAIMED_DRAFT::DESCRIPTION
  name: Dropbox Unclaimed Draft API
  slug: dropbox-unclaimed-draft-api
- description: This namespace contains endpoints and data types for user management.
  name: Dropbox Users API
  slug: dropbox-users-api
artifact_total: 384
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dropbox-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/dropbox-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dropbox-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dropbox-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dropbox
- group: start
  title: ''
  type: Portal
  url: https://www.dropbox.com/developers
- group: operate
  title: ''
  type: Support
  url: https://www.dropbox.com/developers/support
- group: commercial
  title: ''
  type: Plans
  url: https://www.dropbox.com/plans
- group: start
  title: ''
  type: Signup
  url: https://www.dropbox.com/register
- group: docs
  title: ''
  type: Guides
  url: https://www.dropbox.com/developers/reference
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/dropbox/dropbox-api-spec/commits/main
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/dropbox
- group: build
  title: ''
  type: Community SDKs
  url: https://www.dropbox.com/developers/documentation/communitysdks
- group: company
  title: ''
  type: Blog
  url: https://blog.dropbox.com/
created: '2024-06-07T00:00:00.000Z'
description: Dropbox is a file hosting service operated by the American company Dropbox, Inc., headquartered in San Francisco, California, U.S. that offers cloud storage, file synchronization, personal cloud, and client software.
examples:
- key_count: 6
  name: Dropbox Post 2Accountset Profile Photo Example
  slug: dropbox-post-2accountset-profile-photo-example
- key_count: 6
  name: Dropbox Post 2Authtokenfrom Oauth1 Example
  slug: dropbox-post-2authtokenfrom-oauth1-example
- key_count: 6
  name: Dropbox Post 2Checkapp Example
  slug: dropbox-post-2checkapp-example
- key_count: 6
  name: Dropbox Post 2Checkuser Example
  slug: dropbox-post-2checkuser-example
- key_count: 6
  name: Dropbox Post 2File Propertiespropertiessearch Example
  slug: dropbox-post-2file-propertiespropertiessearch-example
- key_count: 6
  name: Dropbox Post 2File Propertiespropertiessearchcontinue Example
  slug: dropbox-post-2file-propertiespropertiessearchcontinue-example
- key_count: 6
  name: Dropbox Post 2File Propertiestemplatesadd For Team Example
  slug: dropbox-post-2file-propertiestemplatesadd-for-team-example
- key_count: 6
  name: Dropbox Post 2File Propertiestemplatesadd For User Example
  slug: dropbox-post-2file-propertiestemplatesadd-for-user-example
- key_count: 6
  name: Dropbox Post 2File Propertiestemplatesget For Team Example
  slug: dropbox-post-2file-propertiestemplatesget-for-team-example
- key_count: 6
  name: Dropbox Post 2File Propertiestemplatesget For User Example
  slug: dropbox-post-2file-propertiestemplatesget-for-user-example
- key_count: 6
  name: Dropbox Post 2File Propertiestemplateslist For Team Example
  slug: dropbox-post-2file-propertiestemplateslist-for-team-example
- key_count: 6
  name: Dropbox Post 2File Propertiestemplateslist For User Example
  slug: dropbox-post-2file-propertiestemplateslist-for-user-example
- key_count: 6
  name: Dropbox Post 2File Propertiestemplatesupdate For Team Example
  slug: dropbox-post-2file-propertiestemplatesupdate-for-team-example
- key_count: 6
  name: Dropbox Post 2File Propertiestemplatesupdate For User Example
  slug: dropbox-post-2file-propertiestemplatesupdate-for-user-example
- key_count: 6
  name: Dropbox Post 2File Requestscount Example
  slug: dropbox-post-2file-requestscount-example
- key_count: 6
  name: Dropbox Post 2File Requestscreate Example
  slug: dropbox-post-2file-requestscreate-example
- key_count: 6
  name: Dropbox Post 2File Requestsdelete All Closed Example
  slug: dropbox-post-2file-requestsdelete-all-closed-example
- key_count: 6
  name: Dropbox Post 2File Requestsdelete Example
  slug: dropbox-post-2file-requestsdelete-example
- key_count: 6
  name: Dropbox Post 2File Requestsget Example
  slug: dropbox-post-2file-requestsget-example
- key_count: 6
  name: Dropbox Post 2File Requestslist V2 Example
  slug: dropbox-post-2file-requestslist-v2-example
- key_count: 6
  name: Dropbox Post 2File Requestslistcontinue Example
  slug: dropbox-post-2file-requestslistcontinue-example
- key_count: 6
  name: Dropbox Post 2File Requestsupdate Example
  slug: dropbox-post-2file-requestsupdate-example
- key_count: 6
  name: Dropbox Post 2Filescopy Batch V2 Example
  slug: dropbox-post-2filescopy-batch-v2-example
- key_count: 6
  name: Dropbox Post 2Filescopy Batchcheck V2 Example
  slug: dropbox-post-2filescopy-batchcheck-v2-example
- key_count: 6
  name: Dropbox Post 2Filescopy Referenceget Example
  slug: dropbox-post-2filescopy-referenceget-example
- key_count: 6
  name: Dropbox Post 2Filescopy Referencesave Example
  slug: dropbox-post-2filescopy-referencesave-example
- key_count: 6
  name: Dropbox Post 2Filescopy V2 Example
  slug: dropbox-post-2filescopy-v2-example
- key_count: 6
  name: Dropbox Post 2Filescreate Folder Batch Example
  slug: dropbox-post-2filescreate-folder-batch-example
- key_count: 6
  name: Dropbox Post 2Filescreate Folder Batchcheck Example
  slug: dropbox-post-2filescreate-folder-batchcheck-example
- key_count: 6
  name: Dropbox Post 2Filescreate Folder V2 Example
  slug: dropbox-post-2filescreate-folder-v2-example
- key_count: 6
  name: Dropbox Post 2Filesdelete Batch Example
  slug: dropbox-post-2filesdelete-batch-example
- key_count: 6
  name: Dropbox Post 2Filesdelete Batchcheck Example
  slug: dropbox-post-2filesdelete-batchcheck-example
- key_count: 6
  name: Dropbox Post 2Filesdelete V2 Example
  slug: dropbox-post-2filesdelete-v2-example
- key_count: 6
  name: Dropbox Post 2Filesdownload Example
  slug: dropbox-post-2filesdownload-example
- key_count: 6
  name: Dropbox Post 2Filesdownload Zip Example
  slug: dropbox-post-2filesdownload-zip-example
- key_count: 6
  name: Dropbox Post 2Filesexport Example
  slug: dropbox-post-2filesexport-example
- key_count: 6
  name: Dropbox Post 2Filesget File Lock Batch Example
  slug: dropbox-post-2filesget-file-lock-batch-example
- key_count: 6
  name: Dropbox Post 2Filesget Metadata Example
  slug: dropbox-post-2filesget-metadata-example
- key_count: 6
  name: Dropbox Post 2Filesget Preview Example
  slug: dropbox-post-2filesget-preview-example
- key_count: 6
  name: Dropbox Post 2Filesget Temporary Link Example
  slug: dropbox-post-2filesget-temporary-link-example
- key_count: 6
  name: Dropbox Post 2Filesget Temporary Upload Link Example
  slug: dropbox-post-2filesget-temporary-upload-link-example
- key_count: 6
  name: Dropbox Post 2Filesget Thumbnail Batch Example
  slug: dropbox-post-2filesget-thumbnail-batch-example
- key_count: 6
  name: Dropbox Post 2Filesget Thumbnail V2 Example
  slug: dropbox-post-2filesget-thumbnail-v2-example
- key_count: 6
  name: Dropbox Post 2Fileslist Folder Example
  slug: dropbox-post-2fileslist-folder-example
- key_count: 6
  name: Dropbox Post 2Fileslist Foldercontinue Example
  slug: dropbox-post-2fileslist-foldercontinue-example
- key_count: 6
  name: Dropbox Post 2Fileslist Folderget Latest Cursor Example
  slug: dropbox-post-2fileslist-folderget-latest-cursor-example
- key_count: 6
  name: Dropbox Post 2Fileslist Folderlongpoll Example
  slug: dropbox-post-2fileslist-folderlongpoll-example
- key_count: 6
  name: Dropbox Post 2Fileslist Revisions Example
  slug: dropbox-post-2fileslist-revisions-example
- key_count: 6
  name: Dropbox Post 2Fileslock File Batch Example
  slug: dropbox-post-2fileslock-file-batch-example
- key_count: 6
  name: Dropbox Post 2Filesmove Batch V2 Example
  slug: dropbox-post-2filesmove-batch-v2-example
- key_count: 6
  name: Dropbox Post 2Filesmove Batchcheck V2 Example
  slug: dropbox-post-2filesmove-batchcheck-v2-example
- key_count: 6
  name: Dropbox Post 2Filesmove V2 Example
  slug: dropbox-post-2filesmove-v2-example
- key_count: 6
  name: Dropbox Post 2Filesrestore Example
  slug: dropbox-post-2filesrestore-example
- key_count: 6
  name: Dropbox Post 2Filessave Url Example
  slug: dropbox-post-2filessave-url-example
- key_count: 6
  name: Dropbox Post 2Filessave Urlcheck Job Status Example
  slug: dropbox-post-2filessave-urlcheck-job-status-example
- key_count: 6
  name: Dropbox Post 2Filessearch V2 Example
  slug: dropbox-post-2filessearch-v2-example
- key_count: 6
  name: Dropbox Post 2Filessearchcontinue V2 Example
  slug: dropbox-post-2filessearchcontinue-v2-example
- key_count: 6
  name: Dropbox Post 2Filesunlock File Batch Example
  slug: dropbox-post-2filesunlock-file-batch-example
- key_count: 6
  name: Dropbox Post 2Filesupload Example
  slug: dropbox-post-2filesupload-example
- key_count: 6
  name: Dropbox Post 2Filesupload Sessionfinish Batch Example
  slug: dropbox-post-2filesupload-sessionfinish-batch-example
- key_count: 6
  name: Dropbox Post 2Filesupload Sessionfinish Batchcheck Example
  slug: dropbox-post-2filesupload-sessionfinish-batchcheck-example
- key_count: 6
  name: Dropbox Post 2Filesupload Sessionfinish Example
  slug: dropbox-post-2filesupload-sessionfinish-example
- key_count: 6
  name: Dropbox Post 2Filesupload Sessionstart Example
  slug: dropbox-post-2filesupload-sessionstart-example
- key_count: 6
  name: Dropbox Post 2Sharingadd File Member Example
  slug: dropbox-post-2sharingadd-file-member-example
- key_count: 6
  name: Dropbox Post 2Sharingcheck Job Status Example
  slug: dropbox-post-2sharingcheck-job-status-example
- key_count: 6
  name: Dropbox Post 2Sharingcheck Remove Member Job Status Example
  slug: dropbox-post-2sharingcheck-remove-member-job-status-example
- key_count: 6
  name: Dropbox Post 2Sharingcheck Share Job Status Example
  slug: dropbox-post-2sharingcheck-share-job-status-example
- key_count: 6
  name: Dropbox Post 2Sharingget File Metadata Example
  slug: dropbox-post-2sharingget-file-metadata-example
- key_count: 6
  name: Dropbox Post 2Sharingget File Metadatabatch Example
  slug: dropbox-post-2sharingget-file-metadatabatch-example
- key_count: 6
  name: Dropbox Post 2Sharingget Folder Metadata Example
  slug: dropbox-post-2sharingget-folder-metadata-example
- key_count: 6
  name: Dropbox Post 2Sharingget Shared Link File Example
  slug: dropbox-post-2sharingget-shared-link-file-example
- key_count: 6
  name: Dropbox Post 2Sharingget Shared Link Metadata Example
  slug: dropbox-post-2sharingget-shared-link-metadata-example
- key_count: 6
  name: Dropbox Post 2Sharinglist File Members Example
  slug: dropbox-post-2sharinglist-file-members-example
- key_count: 6
  name: Dropbox Post 2Sharinglist File Membersbatch Example
  slug: dropbox-post-2sharinglist-file-membersbatch-example
- key_count: 6
  name: Dropbox Post 2Sharinglist File Memberscontinue Example
  slug: dropbox-post-2sharinglist-file-memberscontinue-example
- key_count: 6
  name: Dropbox Post 2Sharinglist Folder Memberscontinue Example
  slug: dropbox-post-2sharinglist-folder-memberscontinue-example
- key_count: 6
  name: Dropbox Post 2Sharinglist Folders Example
  slug: dropbox-post-2sharinglist-folders-example
- key_count: 6
  name: Dropbox Post 2Sharinglist Folderscontinue Example
  slug: dropbox-post-2sharinglist-folderscontinue-example
- key_count: 6
  name: Dropbox Post 2Sharinglist Mountable Folders Example
  slug: dropbox-post-2sharinglist-mountable-folders-example
- key_count: 6
  name: Dropbox Post 2Sharinglist Mountable Folderscontinue Example
  slug: dropbox-post-2sharinglist-mountable-folderscontinue-example
- key_count: 6
  name: Dropbox Post 2Sharinglist Received Files Example
  slug: dropbox-post-2sharinglist-received-files-example
- key_count: 6
  name: Dropbox Post 2Sharinglist Received Filescontinue Example
  slug: dropbox-post-2sharinglist-received-filescontinue-example
- key_count: 6
  name: Dropbox Post 2Sharinglist Shared Links Example
  slug: dropbox-post-2sharinglist-shared-links-example
- key_count: 6
  name: Dropbox Post 2Sharingmodify Shared Link Settings Example
  slug: dropbox-post-2sharingmodify-shared-link-settings-example
- key_count: 6
  name: Dropbox Post 2Sharingmount Folder Example
  slug: dropbox-post-2sharingmount-folder-example
- key_count: 6
  name: Dropbox Post 2Sharingrelinquish Folder Membership Example
  slug: dropbox-post-2sharingrelinquish-folder-membership-example
- key_count: 6
  name: Dropbox Post 2Sharingremove File Member 2 Example
  slug: dropbox-post-2sharingremove-file-member-2-example
- key_count: 6
  name: Dropbox Post 2Sharingremove Folder Member Example
  slug: dropbox-post-2sharingremove-folder-member-example
- key_count: 6
  name: Dropbox Post 2Sharingset Access Inheritance Example
  slug: dropbox-post-2sharingset-access-inheritance-example
- key_count: 6
  name: Dropbox Post 2Sharingshare Folder Example
  slug: dropbox-post-2sharingshare-folder-example
- key_count: 6
  name: Dropbox Post 2Sharingunshare Folder Example
  slug: dropbox-post-2sharingunshare-folder-example
- key_count: 6
  name: Dropbox Post 2Sharingupdate File Member Example
  slug: dropbox-post-2sharingupdate-file-member-example
- key_count: 6
  name: Dropbox Post 2Sharingupdate Folder Member Example
  slug: dropbox-post-2sharingupdate-folder-member-example
- key_count: 6
  name: Dropbox Post 2Sharingupdate Folder Policy Example
  slug: dropbox-post-2sharingupdate-folder-policy-example
- key_count: 6
  name: Dropbox Post 2Team Logget Events Example
  slug: dropbox-post-2team-logget-events-example
- key_count: 6
  name: Dropbox Post 2Team Logget Eventscontinue Example
  slug: dropbox-post-2team-logget-eventscontinue-example
- key_count: 6
  name: Dropbox Post 2Teamfeaturesget Values Example
  slug: dropbox-post-2teamfeaturesget-values-example
- key_count: 6
  name: Dropbox Post 2Teamget Info Example
  slug: dropbox-post-2teamget-info-example
- key_count: 6
  name: Dropbox Post 2Teamgroupscreate Example
  slug: dropbox-post-2teamgroupscreate-example
- key_count: 6
  name: Dropbox Post 2Teamgroupsdelete Example
  slug: dropbox-post-2teamgroupsdelete-example
- key_count: 6
  name: Dropbox Post 2Teamgroupsget Info Example
  slug: dropbox-post-2teamgroupsget-info-example
- key_count: 6
  name: Dropbox Post 2Teamgroupsjob Statusget Example
  slug: dropbox-post-2teamgroupsjob-statusget-example
- key_count: 6
  name: Dropbox Post 2Teamgroupslist Example
  slug: dropbox-post-2teamgroupslist-example
- key_count: 6
  name: Dropbox Post 2Teamgroupslistcontinue Example
  slug: dropbox-post-2teamgroupslistcontinue-example
- key_count: 6
  name: Dropbox Post 2Teamgroupsmembersadd Example
  slug: dropbox-post-2teamgroupsmembersadd-example
- key_count: 6
  name: Dropbox Post 2Teamgroupsmemberslist Example
  slug: dropbox-post-2teamgroupsmemberslist-example
- key_count: 6
  name: Dropbox Post 2Teamgroupsmemberslistcontinue Example
  slug: dropbox-post-2teamgroupsmemberslistcontinue-example
- key_count: 6
  name: Dropbox Post 2Teamgroupsmembersremove Example
  slug: dropbox-post-2teamgroupsmembersremove-example
- key_count: 6
  name: Dropbox Post 2Teamgroupsmembersset Access Type Example
  slug: dropbox-post-2teamgroupsmembersset-access-type-example
- key_count: 6
  name: Dropbox Post 2Teamgroupsupdate Example
  slug: dropbox-post-2teamgroupsupdate-example
- key_count: 6
  name: Dropbox Post 2Teamlegal Holdscreate Policy Example
  slug: dropbox-post-2teamlegal-holdscreate-policy-example
- key_count: 6
  name: Dropbox Post 2Teamlegal Holdsget Policy Example
  slug: dropbox-post-2teamlegal-holdsget-policy-example
- key_count: 6
  name: Dropbox Post 2Teamlegal Holdslist Held Revisions Continue Example
  slug: dropbox-post-2teamlegal-holdslist-held-revisions-continue-example
- key_count: 6
  name: Dropbox Post 2Teamlegal Holdslist Held Revisions Example
  slug: dropbox-post-2teamlegal-holdslist-held-revisions-example
- key_count: 6
  name: Dropbox Post 2Teamlegal Holdslist Policies Example
  slug: dropbox-post-2teamlegal-holdslist-policies-example
- key_count: 6
  name: Dropbox Post 2Teamlegal Holdsupdate Policy Example
  slug: dropbox-post-2teamlegal-holdsupdate-policy-example
- key_count: 6
  name: Dropbox Post 2Teammember Space Limitsexcluded Usersadd Example
  slug: dropbox-post-2teammember-space-limitsexcluded-usersadd-example
- key_count: 6
  name: Dropbox Post 2Teammember Space Limitsexcluded Userslist Example
  slug: dropbox-post-2teammember-space-limitsexcluded-userslist-example
- key_count: 6
  name: Dropbox Post 2Teammember Space Limitsexcluded Userslistcontinue Example
  slug: dropbox-post-2teammember-space-limitsexcluded-userslistcontinue-example
- key_count: 6
  name: Dropbox Post 2Teammember Space Limitsexcluded Usersremove Example
  slug: dropbox-post-2teammember-space-limitsexcluded-usersremove-example
- key_count: 6
  name: Dropbox Post 2Teammember Space Limitsget Custom Quota Example
  slug: dropbox-post-2teammember-space-limitsget-custom-quota-example
- key_count: 6
  name: Dropbox Post 2Teammember Space Limitsremove Custom Quota Example
  slug: dropbox-post-2teammember-space-limitsremove-custom-quota-example
- key_count: 6
  name: Dropbox Post 2Teammember Space Limitsset Custom Quota Example
  slug: dropbox-post-2teammember-space-limitsset-custom-quota-example
- key_count: 6
  name: Dropbox Post 2Teammembersadd Example
  slug: dropbox-post-2teammembersadd-example
- key_count: 6
  name: Dropbox Post 2Teammembersaddjob Statusget Example
  slug: dropbox-post-2teammembersaddjob-statusget-example
- key_count: 6
  name: Dropbox Post 2Teammembersdelete Profile Photo Example
  slug: dropbox-post-2teammembersdelete-profile-photo-example
- key_count: 6
  name: Dropbox Post 2Teammembersget Info Example
  slug: dropbox-post-2teammembersget-info-example
- key_count: 6
  name: Dropbox Post 2Teammemberslist Example
  slug: dropbox-post-2teammemberslist-example
- key_count: 6
  name: Dropbox Post 2Teammemberslistcontinue Example
  slug: dropbox-post-2teammemberslistcontinue-example
- key_count: 6
  name: Dropbox Post 2Teammembersmove Former Member Files Example
  slug: dropbox-post-2teammembersmove-former-member-files-example
- key_count: 6
  name: Dropbox Post 2Teammembersmove Former Member Filesjob Statuscheck Example
  slug: dropbox-post-2teammembersmove-former-member-filesjob-statuscheck-example
- key_count: 6
  name: Dropbox Post 2Teammembersremove Example
  slug: dropbox-post-2teammembersremove-example
- key_count: 6
  name: Dropbox Post 2Teammembersremovejob Statusget Example
  slug: dropbox-post-2teammembersremovejob-statusget-example
- key_count: 6
  name: Dropbox Post 2Teammemberssecondary Emailsadd Example
  slug: dropbox-post-2teammemberssecondary-emailsadd-example
- key_count: 6
  name: Dropbox Post 2Teammemberssecondary Emailsdelete Example
  slug: dropbox-post-2teammemberssecondary-emailsdelete-example
- key_count: 6
  name: Dropbox Post 2Teammemberssecondary Emailsresend Verification Emails Example
  slug: dropbox-post-2teammemberssecondary-emailsresend-verification-emails-example
- key_count: 6
  name: Dropbox Post 2Teammembersset Admin Permissions Example
  slug: dropbox-post-2teammembersset-admin-permissions-example
- key_count: 6
  name: Dropbox Post 2Teammembersset Profile Example
  slug: dropbox-post-2teammembersset-profile-example
- key_count: 6
  name: Dropbox Post 2Teammembersset Profile Photo Example
  slug: dropbox-post-2teammembersset-profile-photo-example
- key_count: 6
  name: Dropbox Post 2Teamnamespaceslist Example
  slug: dropbox-post-2teamnamespaceslist-example
- key_count: 6
  name: Dropbox Post 2Teamnamespaceslistcontinue Example
  slug: dropbox-post-2teamnamespaceslistcontinue-example
- key_count: 6
  name: Dropbox Post 2Teamteam Folderactivate Example
  slug: dropbox-post-2teamteam-folderactivate-example
- key_count: 6
  name: Dropbox Post 2Teamteam Folderarchive Example
  slug: dropbox-post-2teamteam-folderarchive-example
- key_count: 6
  name: Dropbox Post 2Teamteam Folderarchivecheck Example
  slug: dropbox-post-2teamteam-folderarchivecheck-example
- key_count: 6
  name: Dropbox Post 2Teamteam Foldercreate Example
  slug: dropbox-post-2teamteam-foldercreate-example
- key_count: 6
  name: Dropbox Post 2Teamteam Folderlist Example
  slug: dropbox-post-2teamteam-folderlist-example
- key_count: 6
  name: Dropbox Post 2Teamteam Folderlistcontinue Example
  slug: dropbox-post-2teamteam-folderlistcontinue-example
- key_count: 6
  name: Dropbox Post 2Teamteam Folderrename Example
  slug: dropbox-post-2teamteam-folderrename-example
- key_count: 6
  name: Dropbox Post 2Teamteam Folderupdate Sync Settings Example
  slug: dropbox-post-2teamteam-folderupdate-sync-settings-example
- key_count: 6
  name: Dropbox Post 2Teamtokenget Authenticated Admin Example
  slug: dropbox-post-2teamtokenget-authenticated-admin-example
- key_count: 6
  name: Dropbox Post 2Usersfeaturesget Values Example
  slug: dropbox-post-2usersfeaturesget-values-example
- key_count: 6
  name: Dropbox Post 2Usersget Account Batch Example
  slug: dropbox-post-2usersget-account-batch-example
- key_count: 6
  name: Dropbox Post 2Usersget Account Example
  slug: dropbox-post-2usersget-account-example
- key_count: 6
  name: Dropbox Post 2Usersget Current Account Example
  slug: dropbox-post-2usersget-current-account-example
- key_count: 6
  name: Dropbox Post 2Usersget Space Usage Example
  slug: dropbox-post-2usersget-space-usage-example
features:
- Standard at $15/user/mo with 3 TB pooled storage
- Advanced at $24/user/mo with 15 TB and end-to-end encryption
- 180-day (Standard) or 1-year (Advanced) deleted-file recovery
- 100 GB Transfer for large file delivery
- Dropbox Sign integrated PDF signatures
- REST API at api.dropboxapi.com/2/
- Default 1,200 req/min per app rate limit
- OAuth 2.0 with team and individual scopes
- Webhooks for file change notifications
- List folder with cursor-based pagination
- Paper for collaborative documents
- Capture for screen recording
- Replay for video review
- Tiered admin (Advanced)
- SSO, SCIM provisioning (Advanced)
- Compliance tracking and EKM (Advanced)
finops:
- name: Dropbox Finops
  service_category: File Storage
  slug: dropbox-finops
graphqls:
- description: This conceptual GraphQL schema models the Dropbox cloud file storage REST API
  name: Dropbox GraphQL Schema
  slug: dropbox-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dropbox.png
json_schemas:
- name: AccountCreateRequest
  property_count: 4
  slug: dropbox-accountcreaterequest
- name: AccountCreateResponse
  property_count: 3
  slug: dropbox-accountcreateresponse
- name: AccountGetResponse
  property_count: 2
  slug: dropbox-accountgetresponse
- name: AccountResponse
  property_count: 10
  slug: dropbox-accountresponse
- name: AccountResponseQuotas
  property_count: 5
  slug: dropbox-accountresponsequotas
- name: AccountUpdateRequest
  property_count: 3
  slug: dropbox-accountupdaterequest
- name: AccountVerifyRequest
  property_count: 1
  slug: dropbox-accountverifyrequest
- name: AccountVerifyResponse
  property_count: 2
  slug: dropbox-accountverifyresponse
- name: AccountVerifyResponseAccount
  property_count: 1
  slug: dropbox-accountverifyresponseaccount
- name: ApiAppCreateRequest
  property_count: 7
  slug: dropbox-apiappcreaterequest
- name: ApiAppGetResponse
  property_count: 2
  slug: dropbox-apiappgetresponse
- name: ApiAppListResponse
  property_count: 3
  slug: dropbox-apiapplistresponse
- name: ApiAppResponse
  property_count: 10
  slug: dropbox-apiappresponse
- name: ApiAppResponseOAuth
  property_count: 4
  slug: dropbox-apiappresponseoauth
- name: ApiAppResponseOptions
  property_count: 1
  slug: dropbox-apiappresponseoptions
- name: ApiAppResponseOwnerAccount
  property_count: 2
  slug: dropbox-apiappresponseowneraccount
- name: ApiAppResponseWhiteLabelingOptions
  property_count: 14
  slug: dropbox-apiappresponsewhitelabelingoptions
- name: ApiAppUpdateRequest
  property_count: 7
  slug: dropbox-apiappupdaterequest
- name: BulkSendJobGetResponse
  property_count: 4
  slug: dropbox-bulksendjobgetresponse
- name: BulkSendJobGetResponseSignatureRequests
  property_count: 0
  slug: dropbox-bulksendjobgetresponsesignaturerequests
- name: BulkSendJobListResponse
  property_count: 3
  slug: dropbox-bulksendjoblistresponse
- name: BulkSendJobResponse
  property_count: 4
  slug: dropbox-bulksendjobresponse
- name: BulkSendJobSendResponse
  property_count: 2
  slug: dropbox-bulksendjobsendresponse
- name: EmbeddedEditUrlRequest
  property_count: 10
  slug: dropbox-embeddedediturlrequest
- name: EmbeddedEditUrlResponse
  property_count: 2
  slug: dropbox-embeddedediturlresponse
- name: EmbeddedEditUrlResponseEmbedded
  property_count: 2
  slug: dropbox-embeddedediturlresponseembedded
- name: EmbeddedSignUrlResponse
  property_count: 2
  slug: dropbox-embeddedsignurlresponse
- name: EmbeddedSignUrlResponseEmbedded
  property_count: 2
  slug: dropbox-embeddedsignurlresponseembedded
- name: ErrorResponse
  property_count: 1
  slug: dropbox-errorresponse
- name: ErrorResponseError
  property_count: 3
  slug: dropbox-errorresponseerror
- name: EventCallbackRequest
  property_count: 4
  slug: dropbox-eventcallbackrequest
- name: EventCallbackRequestEvent
  property_count: 4
  slug: dropbox-eventcallbackrequestevent
- name: EventCallbackRequestEventMetadata
  property_count: 4
  slug: dropbox-eventcallbackrequesteventmetadata
- name: FileResponse
  property_count: 2
  slug: dropbox-fileresponse
- name: FileResponseDataUri
  property_count: 1
  slug: dropbox-fileresponsedatauri
- name: ListInfoResponse
  property_count: 4
  slug: dropbox-listinforesponse
- name: OAuthTokenGenerateRequest
  property_count: 5
  slug: dropbox-oauthtokengeneraterequest
- name: OAuthTokenRefreshRequest
  property_count: 2
  slug: dropbox-oauthtokenrefreshrequest
- name: OAuthTokenResponse
  property_count: 5
  slug: dropbox-oauthtokenresponse
- name: ReportCreateRequest
  property_count: 3
  slug: dropbox-reportcreaterequest
- name: ReportCreateResponse
  property_count: 2
  slug: dropbox-reportcreateresponse
- name: ReportResponse
  property_count: 4
  slug: dropbox-reportresponse
- name: SignatureRequestBulkCreateEmbeddedWithTemplateRequest
  property_count: 13
  slug: dropbox-signaturerequestbulkcreateembeddedwithtemplaterequest
- name: SignatureRequestBulkSendWithTemplateRequest
  property_count: 13
  slug: dropbox-signaturerequestbulksendwithtemplaterequest
- name: SignatureRequestCreateEmbeddedRequest
  property_count: 24
  slug: dropbox-signaturerequestcreateembeddedrequest
- name: SignatureRequestCreateEmbeddedWithTemplateRequest
  property_count: 15
  slug: dropbox-signaturerequestcreateembeddedwithtemplaterequest
- name: SignatureRequestEditEmbeddedRequest
  property_count: 24
  slug: dropbox-signaturerequesteditembeddedrequest
- name: SignatureRequestEditEmbeddedWithTemplateRequest
  property_count: 15
  slug: dropbox-signaturerequesteditembeddedwithtemplaterequest
- name: SignatureRequestEditRequest
  property_count: 26
  slug: dropbox-signaturerequesteditrequest
- name: SignatureRequestEditWithTemplateRequest
  property_count: 17
  slug: dropbox-signaturerequesteditwithtemplaterequest
- name: SignatureRequestGetResponse
  property_count: 2
  slug: dropbox-signaturerequestgetresponse
- name: SignatureRequestListResponse
  property_count: 3
  slug: dropbox-signaturerequestlistresponse
- name: SignatureRequestRemindRequest
  property_count: 2
  slug: dropbox-signaturerequestremindrequest
- name: SignatureRequestResponse
  property_count: 25
  slug: dropbox-signaturerequestresponse
- name: SignatureRequestResponseAttachment
  property_count: 6
  slug: dropbox-signaturerequestresponseattachment
- name: SignatureRequestResponseCustomFieldBase
  property_count: 5
  slug: dropbox-signaturerequestresponsecustomfieldbase
- name: SignatureRequestResponseCustomFieldCheckbox
  property_count: 0
  slug: dropbox-signaturerequestresponsecustomfieldcheckbox
- name: SignatureRequestResponseCustomFieldText
  property_count: 0
  slug: dropbox-signaturerequestresponsecustomfieldtext
- name: SignatureRequestResponseCustomFieldTypeEnum
  property_count: 0
  slug: dropbox-signaturerequestresponsecustomfieldtypeenum
- name: SignatureRequestResponseDataBase
  property_count: 5
  slug: dropbox-signaturerequestresponsedatabase
- name: SignatureRequestResponseDataTypeEnum
  property_count: 0
  slug: dropbox-signaturerequestresponsedatatypeenum
- name: SignatureRequestResponseDataValueCheckbox
  property_count: 0
  slug: dropbox-signaturerequestresponsedatavaluecheckbox
- name: SignatureRequestResponseDataValueCheckboxMerge
  property_count: 0
  slug: dropbox-signaturerequestresponsedatavaluecheckboxmerge
- name: SignatureRequestResponseDataValueDateSigned
  property_count: 0
  slug: dropbox-signaturerequestresponsedatavaluedatesigned
- name: SignatureRequestResponseDataValueDropdown
  property_count: 0
  slug: dropbox-signaturerequestresponsedatavaluedropdown
- name: SignatureRequestResponseDataValueInitials
  property_count: 0
  slug: dropbox-signaturerequestresponsedatavalueinitials
- name: SignatureRequestResponseDataValueRadio
  property_count: 0
  slug: dropbox-signaturerequestresponsedatavalueradio
- name: SignatureRequestResponseDataValueSignature
  property_count: 0
  slug: dropbox-signaturerequestresponsedatavaluesignature
- name: SignatureRequestResponseDataValueText
  property_count: 0
  slug: dropbox-signaturerequestresponsedatavaluetext
- name: SignatureRequestResponseDataValueTextMerge
  property_count: 0
  slug: dropbox-signaturerequestresponsedatavaluetextmerge
- name: SignatureRequestResponseSignatures
  property_count: 19
  slug: dropbox-signaturerequestresponsesignatures
- name: SignatureRequestSendRequest
  property_count: 26
  slug: dropbox-signaturerequestsendrequest
- name: SignatureRequestSendWithTemplateRequest
  property_count: 17
  slug: dropbox-signaturerequestsendwithtemplaterequest
- name: SignatureRequestUpdateRequest
  property_count: 4
  slug: dropbox-signaturerequestupdaterequest
- name: SubAttachment
  property_count: 4
  slug: dropbox-subattachment
- name: SubBulkSignerList
  property_count: 2
  slug: dropbox-subbulksignerlist
- name: SubBulkSignerListCustomField
  property_count: 2
  slug: dropbox-subbulksignerlistcustomfield
- name: SubCC
  property_count: 2
  slug: dropbox-subcc
- name: SubCustomField
  property_count: 4
  slug: dropbox-subcustomfield
- name: SubEditorOptions
  property_count: 2
  slug: dropbox-subeditoroptions
- name: SubFieldOptions
  property_count: 1
  slug: dropbox-subfieldoptions
- name: SubFormFieldGroup
  property_count: 3
  slug: dropbox-subformfieldgroup
- name: SubFormFieldRule
  property_count: 4
  slug: dropbox-subformfieldrule
- name: SubFormFieldRuleAction
  property_count: 4
  slug: dropbox-subformfieldruleaction
- name: SubFormFieldRuleTrigger
  property_count: 4
  slug: dropbox-subformfieldruletrigger
- name: SubFormFieldsPerDocumentBase
  property_count: 11
  slug: dropbox-subformfieldsperdocumentbase
- name: SubFormFieldsPerDocumentCheckbox
  property_count: 0
  slug: dropbox-subformfieldsperdocumentcheckbox
- name: SubFormFieldsPerDocumentCheckboxMerge
  property_count: 0
  slug: dropbox-subformfieldsperdocumentcheckboxmerge
- name: SubFormFieldsPerDocumentDateSigned
  property_count: 0
  slug: dropbox-subformfieldsperdocumentdatesigned
- name: SubFormFieldsPerDocumentDropdown
  property_count: 0
  slug: dropbox-subformfieldsperdocumentdropdown
- name: SubFormFieldsPerDocumentFontEnum
  property_count: 0
  slug: dropbox-subformfieldsperdocumentfontenum
- name: SubFormFieldsPerDocumentHyperlink
  property_count: 0
  slug: dropbox-subformfieldsperdocumenthyperlink
- name: SubFormFieldsPerDocumentInitials
  property_count: 0
  slug: dropbox-subformfieldsperdocumentinitials
- name: SubFormFieldsPerDocumentRadio
  property_count: 0
  slug: dropbox-subformfieldsperdocumentradio
- name: SubFormFieldsPerDocumentSignature
  property_count: 0
  slug: dropbox-subformfieldsperdocumentsignature
- name: SubFormFieldsPerDocumentText
  property_count: 0
  slug: dropbox-subformfieldsperdocumenttext
- name: SubFormFieldsPerDocumentTextMerge
  property_count: 0
  slug: dropbox-subformfieldsperdocumenttextmerge
- name: SubFormFieldsPerDocumentTypeEnum
  property_count: 0
  slug: dropbox-subformfieldsperdocumenttypeenum
- name: SubMergeField
  property_count: 2
  slug: dropbox-submergefield
- name: SubOAuth
  property_count: 2
  slug: dropbox-suboauth
- name: SubOptions
  property_count: 1
  slug: dropbox-suboptions
- name: SubSignatureRequestGroupedSigners
  property_count: 3
  slug: dropbox-subsignaturerequestgroupedsigners
- name: SubSignatureRequestSigner
  property_count: 6
  slug: dropbox-subsignaturerequestsigner
- name: SubSignatureRequestTemplateSigner
  property_count: 6
  slug: dropbox-subsignaturerequesttemplatesigner
- name: SubSigningOptions
  property_count: 5
  slug: dropbox-subsigningoptions
- name: SubTeamResponse
  property_count: 2
  slug: dropbox-subteamresponse
- name: SubTemplateRole
  property_count: 2
  slug: dropbox-subtemplaterole
- name: SubUnclaimedDraftSigner
  property_count: 3
  slug: dropbox-subunclaimeddraftsigner
- name: SubUnclaimedDraftTemplateSigner
  property_count: 3
  slug: dropbox-subunclaimeddrafttemplatesigner
- name: SubWhiteLabelingOptions
  property_count: 15
  slug: dropbox-subwhitelabelingoptions
- name: TeamAddMemberRequest
  property_count: 3
  slug: dropbox-teamaddmemberrequest
- name: TeamCreateRequest
  property_count: 1
  slug: dropbox-teamcreaterequest
- name: TeamGetInfoResponse
  property_count: 2
  slug: dropbox-teamgetinforesponse
- name: TeamGetResponse
  property_count: 2
  slug: dropbox-teamgetresponse
- name: TeamInfoResponse
  property_count: 5
  slug: dropbox-teaminforesponse
- name: TeamInviteResponse
  property_count: 6
  slug: dropbox-teaminviteresponse
- name: TeamInvitesResponse
  property_count: 2
  slug: dropbox-teaminvitesresponse
- name: TeamMemberResponse
  property_count: 3
  slug: dropbox-teammemberresponse
- name: TeamMembersResponse
  property_count: 3
  slug: dropbox-teammembersresponse
- name: TeamParentResponse
  property_count: 2
  slug: dropbox-teamparentresponse
- name: TeamRemoveMemberRequest
  property_count: 5
  slug: dropbox-teamremovememberrequest
- name: TeamResponse
  property_count: 4
  slug: dropbox-teamresponse
- name: TeamSubTeamsResponse
  property_count: 3
  slug: dropbox-teamsubteamsresponse
- name: TeamUpdateRequest
  property_count: 1
  slug: dropbox-teamupdaterequest
- name: TemplateAddUserRequest
  property_count: 3
  slug: dropbox-templateadduserrequest
- name: TemplateCreateEmbeddedDraftRequest
  property_count: 25
  slug: dropbox-templatecreateembeddeddraftrequest
- name: TemplateCreateEmbeddedDraftResponse
  property_count: 2
  slug: dropbox-templatecreateembeddeddraftresponse
- name: TemplateCreateEmbeddedDraftResponseTemplate
  property_count: 4
  slug: dropbox-templatecreateembeddeddraftresponsetemplate
- name: TemplateCreateRequest
  property_count: 18
  slug: dropbox-templatecreaterequest
- name: TemplateCreateResponse
  property_count: 2
  slug: dropbox-templatecreateresponse
- name: TemplateCreateResponseTemplate
  property_count: 1
  slug: dropbox-templatecreateresponsetemplate
- name: TemplateEditResponse
  property_count: 1
  slug: dropbox-templateeditresponse
- name: TemplateGetResponse
  property_count: 2
  slug: dropbox-templategetresponse
- name: TemplateListResponse
  property_count: 3
  slug: dropbox-templatelistresponse
- name: TemplateRemoveUserRequest
  property_count: 2
  slug: dropbox-templateremoveuserrequest
- name: TemplateResponse
  property_count: 15
  slug: dropbox-templateresponse
- name: TemplateResponseAccount
  property_count: 6
  slug: dropbox-templateresponseaccount
- name: TemplateResponseAccountQuota
  property_count: 4
  slug: dropbox-templateresponseaccountquota
- name: TemplateResponseCCRole
  property_count: 1
  slug: dropbox-templateresponseccrole
- name: TemplateResponseDocument
  property_count: 6
  slug: dropbox-templateresponsedocument
- name: TemplateResponseDocumentCustomFieldBase
  property_count: 10
  slug: dropbox-templateresponsedocumentcustomfieldbase
- name: TemplateResponseDocumentCustomFieldCheckbox
  property_count: 0
  slug: dropbox-templateresponsedocumentcustomfieldcheckbox
- name: TemplateResponseDocumentCustomFieldText
  property_count: 0
  slug: dropbox-templateresponsedocumentcustomfieldtext
- name: TemplateResponseDocumentFieldGroup
  property_count: 2
  slug: dropbox-templateresponsedocumentfieldgroup
- name: TemplateResponseDocumentFieldGroupRule
  property_count: 2
  slug: dropbox-templateresponsedocumentfieldgrouprule
- name: TemplateResponseDocumentFormFieldBase
  property_count: 10
  slug: dropbox-templateresponsedocumentformfieldbase
- name: TemplateResponseDocumentFormFieldCheckbox
  property_count: 0
  slug: dropbox-templateresponsedocumentformfieldcheckbox
- name: TemplateResponseDocumentFormFieldDateSigned
  property_count: 0
  slug: dropbox-templateresponsedocumentformfielddatesigned
- name: TemplateResponseDocumentFormFieldDropdown
  property_count: 0
  slug: dropbox-templateresponsedocumentformfielddropdown
- name: TemplateResponseDocumentFormFieldHyperlink
  property_count: 0
  slug: dropbox-templateresponsedocumentformfieldhyperlink
- name: TemplateResponseDocumentFormFieldInitials
  property_count: 0
  slug: dropbox-templateresponsedocumentformfieldinitials
- name: TemplateResponseDocumentFormFieldRadio
  property_count: 0
  slug: dropbox-templateresponsedocumentformfieldradio
- name: TemplateResponseDocumentFormFieldSignature
  property_count: 0
  slug: dropbox-templateresponsedocumentformfieldsignature
- name: TemplateResponseDocumentFormFieldText
  property_count: 0
  slug: dropbox-templateresponsedocumentformfieldtext
- name: TemplateResponseDocumentStaticFieldBase
  property_count: 10
  slug: dropbox-templateresponsedocumentstaticfieldbase
- name: TemplateResponseDocumentStaticFieldCheckbox
  property_count: 0
  slug: dropbox-templateresponsedocumentstaticfieldcheckbox
- name: TemplateResponseDocumentStaticFieldDateSigned
  property_count: 0
  slug: dropbox-templateresponsedocumentstaticfielddatesigned
- name: TemplateResponseDocumentStaticFieldDropdown
  property_count: 0
  slug: dropbox-templateresponsedocumentstaticfielddropdown
- name: TemplateResponseDocumentStaticFieldHyperlink
  property_count: 0
  slug: dropbox-templateresponsedocumentstaticfieldhyperlink
- name: TemplateResponseDocumentStaticFieldInitials
  property_count: 0
  slug: dropbox-templateresponsedocumentstaticfieldinitials
- name: TemplateResponseDocumentStaticFieldRadio
  property_count: 0
  slug: dropbox-templateresponsedocumentstaticfieldradio
- name: TemplateResponseDocumentStaticFieldSignature
  property_count: 0
  slug: dropbox-templateresponsedocumentstaticfieldsignature
- name: TemplateResponseDocumentStaticFieldText
  property_count: 0
  slug: dropbox-templateresponsedocumentstaticfieldtext
- name: TemplateResponseFieldAvgTextLength
  property_count: 2
  slug: dropbox-templateresponsefieldavgtextlength
- name: TemplateResponseSignerRole
  property_count: 2
  slug: dropbox-templateresponsesignerrole
- name: TemplateUpdateFilesRequest
  property_count: 6
  slug: dropbox-templateupdatefilesrequest
- name: TemplateUpdateFilesResponse
  property_count: 1
  slug: dropbox-templateupdatefilesresponse
- name: TemplateUpdateFilesResponseTemplate
  property_count: 2
  slug: dropbox-templateupdatefilesresponsetemplate
- name: UnclaimedDraftCreateEmbeddedRequest
  property_count: 36
  slug: dropbox-unclaimeddraftcreateembeddedrequest
- name: UnclaimedDraftCreateEmbeddedWithTemplateRequest
  property_count: 30
  slug: dropbox-unclaimeddraftcreateembeddedwithtemplaterequest
- name: UnclaimedDraftCreateRequest
  property_count: 24
  slug: dropbox-unclaimeddraftcreaterequest
- name: UnclaimedDraftCreateResponse
  property_count: 2
  slug: dropbox-unclaimeddraftcreateresponse
- name: UnclaimedDraftEditAndResendRequest
  property_count: 8
  slug: dropbox-unclaimeddrafteditandresendrequest
- name: UnclaimedDraftResponse
  property_count: 6
  slug: dropbox-unclaimeddraftresponse
- name: WarningResponse
  property_count: 2
  slug: dropbox-warningresponse
json_structures:
- name: Dropbox Structure
  property_count: 0
  slug: dropbox-structure
layout: provider
modified: '2026-05-19'
name: Dropbox
nav: Providers
network: true
overview: 'Dropbox publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Account API, Api App API, Auth API, and 25 more. Tagged areas include Documents.


  The Dropbox catalog on APIs.io includes 1 Spectral governance ruleset.


  Dropbox''s developer surface includes authentication, developer portal, support, signup flow, changelog, engineering blog, and 8 more developer resources.'
plans:
- name: Dropbox Plans Pricing
  plan_count: 2
  slug: dropbox-plans-pricing
random_paper: 88
rate_limits:
- limit_count: 3
  name: Dropbox Rate Limits
  slug: dropbox-rate-limits
rules:
- name: Dropbox API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: dropbox-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.0
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 64.4
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 28
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dropbox/refs/heads/main/screenshots/dropbox-2026-06-20T180244.png
security:
- kind: authentication
  name: Dropbox Authentication
  slug: dropbox-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Dropbox Domain Security
  slug: dropbox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Dropbox Trust Center
  slug: dropbox-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, GDPR, CSA STAR
slug: dropbox
tags:
- Documents
website: https://www.dropbox.com/developers
---

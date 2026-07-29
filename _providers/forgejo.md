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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 245
  human_in_the_loop: 5
  name: Forgejo Agentic Access
  operation_count: 506
  slug: forgejo-agentic-access
  summary_line: 506 operations · 245 acting · 5 human-in-the-loop
api_count: 10
apis:
- description: The activitypub API from Forgejo — 11 operation(s) for activitypub.
  name: Forgejo activitypub API
  slug: forgejo-activitypub-api
- description: The admin API from Forgejo — 34 operation(s) for admin.
  name: Forgejo admin API
  slug: forgejo-admin-api
- description: The issue API from Forgejo — 33 operation(s) for issue.
  name: Forgejo issue API
  slug: forgejo-issue-api
- description: The miscellaneous API from Forgejo — 14 operation(s) for miscellaneous.
  name: Forgejo miscellaneous API
  slug: forgejo-miscellaneous-api
- description: The notification API from Forgejo — 4 operation(s) for notification.
  name: Forgejo notification API
  slug: forgejo-notification-api
- description: The organization API from Forgejo — 42 operation(s) for organization.
  name: Forgejo organization API
  slug: forgejo-organization-api
- description: The package API from Forgejo — 5 operation(s) for package.
  name: Forgejo package API
  slug: forgejo-package-api
- description: The repository API from Forgejo — 126 operation(s) for repository.
  name: Forgejo repository API
  slug: forgejo-repository-api
- description: The settings API from Forgejo — 4 operation(s) for settings.
  name: Forgejo settings API
  slug: forgejo-settings-api
- description: The user API from Forgejo — 54 operation(s) for user.
  name: Forgejo user API
  slug: forgejo-user-api
artifact_total: 279
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/forgejo-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/forgejo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forgejo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/forgejo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://forgejo.org
- group: docs
  title: ''
  type: Documentation
  url: https://forgejo.org/docs/latest/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/forgejo
- group: company
  title: ''
  type: Blog
  url: https://forgejo.org/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://forgejo.org/rss.xml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.forgejo.org
- group: other
  title: ''
  type: X
  url: https://floss.social/@forgejo
- group: commercial
  title: ''
  type: Pricing
  url: https://forgejo.org
- group: commercial
  title: ''
  type: Plans
  url: plans/forgejo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/forgejo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/forgejo-finops.yml
- group: build
  title: ''
  type: SourceCode
  url: https://codeberg.org/forgejo/forgejo
- group: other
  title: ''
  type: Donate
  url: https://liberapay.com/forgejo
created: '2026-06-13'
description: Forgejo is a self-hosted lightweight software forge and open-source Git service (a Gitea fork) managed by the non-profit Codeberg e.V. It provides a comprehensive REST API for managing repositories, users, organizations, issues, pull requests, CI/CD workflows via Actions, and package registries. Forgejo emphasizes privacy, low resource usage, and community ownership as a Free Software alternative to centralized code hosting platforms.
examples:
- key_count: 3
  name: Actiontask Example
  slug: actiontask-example
- key_count: 3
  name: Branch Example
  slug: branch-example
- key_count: 3
  name: Commit Example
  slug: commit-example
- key_count: 3
  name: Hook Example
  slug: hook-example
- key_count: 3
  name: Issue Example
  slug: issue-example
- key_count: 3
  name: Label Example
  slug: label-example
- key_count: 3
  name: Milestone Example
  slug: milestone-example
- key_count: 3
  name: Notificationthread Example
  slug: notificationthread-example
- key_count: 3
  name: Organization Example
  slug: organization-example
- key_count: 3
  name: Package Example
  slug: package-example
- key_count: 3
  name: Pullrequest Example
  slug: pullrequest-example
- key_count: 3
  name: Release Example
  slug: release-example
- key_count: 3
  name: Repository Example
  slug: repository-example
- key_count: 3
  name: Team Example
  slug: team-example
- key_count: 3
  name: User Example
  slug: user-example
finops:
- name: Forgejo Finops
  service_category: ''
  slug: forgejo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/forgejo.png
json_schemas:
- name: AccessToken represents an API access token.
  property_count: 7
  slug: accesstoken
- name: ActionArtifact
  property_count: 9
  slug: actionartifact
- name: ActionRun
  property_count: 23
  slug: actionrun
- name: ActionRunJob
  property_count: 11
  slug: actionrunjob
- name: ActionRunner
  property_count: 10
  slug: actionrunner
- name: ActionTask
  property_count: 13
  slug: actiontask
- name: ActionTaskResponse
  property_count: 2
  slug: actiontaskresponse
- name: ActionVariable
  property_count: 4
  slug: actionvariable
- name: Activity
  property_count: 13
  slug: activity
- name: ActivityPub
  property_count: 1
  slug: activitypub
- name: AddCollaboratorOption
  property_count: 1
  slug: addcollaboratoroption
- name: AddTimeOption
  property_count: 3
  slug: addtimeoption
- name: AnnotatedTag
  property_count: 8
  slug: annotatedtag
- name: AnnotatedTagObject
  property_count: 3
  slug: annotatedtagobject
- name: APIError
  property_count: 2
  slug: apierror
- name: APIForbiddenError
  property_count: 2
  slug: apiforbiddenerror
- name: APIInternalServerError
  property_count: 2
  slug: apiinternalservererror
- name: APIInvalidTopicsError
  property_count: 2
  slug: apiinvalidtopicserror
- name: APINotFound
  property_count: 3
  slug: apinotfound
- name: APIRepoArchivedError
  property_count: 2
  slug: apirepoarchivederror
- name: APIUnauthorizedError
  property_count: 2
  slug: apiunauthorizederror
- name: APIValidationError
  property_count: 2
  slug: apivalidationerror
- name: APRemoteFollowOption
  property_count: 1
  slug: apremotefollowoption
- name: Attachment
  property_count: 8
  slug: attachment
- name: BlockedUser represents a blocked user.
  property_count: 2
  slug: blockeduser
- name: Branch
  property_count: 9
  slug: branch
- name: BranchProtection
  property_count: 27
  slug: branchprotection
- name: ChangedFile
  property_count: 9
  slug: changedfile
- name: ChangeFileOperation
  property_count: 5
  slug: changefileoperation
- name: ChangeFilesOptions
  property_count: 9
  slug: changefilesoptions
- name: CombinedStatus
  property_count: 7
  slug: combinedstatus
- name: Comment
  property_count: 11
  slug: comment
- name: Commit contains information generated from a Git commit.
  property_count: 10
  slug: commit
- name: CommitAffectedFiles
  property_count: 2
  slug: commitaffectedfiles
- name: CommitDateOptions
  property_count: 2
  slug: commitdateoptions
- name: CommitMeta contains meta information of a commit in terms of API.
  property_count: 3
  slug: commitmeta
- name: CommitStats
  property_count: 3
  slug: commitstats
- name: CommitStatus
  property_count: 9
  slug: commitstatus
- name: CommitStatusState
  property_count: 0
  slug: commitstatusstate
- name: CommitUser contains information of a user in the context of a commit.
  property_count: 3
  slug: commituser
- name: Compare represents a comparison between two commits.
  property_count: 3
  slug: compare
- name: ContentsResponse
  property_count: 16
  slug: contentsresponse
- name: CreateAccessTokenOption
  property_count: 3
  slug: createaccesstokenoption
- name: CreateBranchProtectionOption
  property_count: 25
  slug: createbranchprotectionoption
- name: CreateBranchRepoOption
  property_count: 3
  slug: createbranchrepooption
- name: CreateEmailOption
  property_count: 1
  slug: createemailoption
- name: CreateFileOptions
  property_count: 9
  slug: createfileoptions
- name: CreateForkOption
  property_count: 2
  slug: createforkoption
- name: CreateGPGKeyOption
  property_count: 2
  slug: creategpgkeyoption
- name: CreateHookOption
  property_count: 6
  slug: createhookoption
- name: CreateHookOptionConfig
  property_count: 0
  slug: createhookoptionconfig
- name: CreateIssueCommentOption
  property_count: 2
  slug: createissuecommentoption
- name: CreateIssueOption
  property_count: 9
  slug: createissueoption
- name: CreateKeyOption
  property_count: 3
  slug: createkeyoption
- name: CreateLabelOption
  property_count: 5
  slug: createlabeloption
- name: CreateMilestoneOption
  property_count: 4
  slug: createmilestoneoption
- name: CreateOAuth2ApplicationOptions
  property_count: 3
  slug: createoauth2applicationoptions
- name: CreateOrgOption
  property_count: 8
  slug: createorgoption
- name: CreateOrUpdateSecretOption defines the properties of the secret to create or update.
  property_count: 1
  slug: createorupdatesecretoption
- name: CreatePullRequestOption
  property_count: 9
  slug: createpullrequestoption
- name: CreatePullReviewComment
  property_count: 5
  slug: createpullreviewcomment
- name: CreatePullReviewCommentOptions
  property_count: 0
  slug: createpullreviewcommentoptions
- name: CreatePullReviewOptions
  property_count: 4
  slug: createpullreviewoptions
- name: CreatePushMirrorOption represents need information to create a push mirror of a repository.
  property_count: 7
  slug: createpushmirroroption
- name: CreateQuotaGroupOptions
  property_count: 2
  slug: createquotagroupoptions
- name: CreateQuotaRuleOptions
  property_count: 3
  slug: createquotaruleoptions
- name: CreateReleaseOption
  property_count: 7
  slug: createreleaseoption
- name: CreateRepoOption
  property_count: 12
  slug: createrepooption
- name: CreateStatusOption
  property_count: 4
  slug: createstatusoption
- name: CreateTagOption
  property_count: 3
  slug: createtagoption
- name: CreateTagProtectionOption
  property_count: 3
  slug: createtagprotectionoption
- name: CreateTeamOption
  property_count: 7
  slug: createteamoption
- name: CreateUserOption
  property_count: 11
  slug: createuseroption
- name: CreateVariableOption defines the properties of the variable to create.
  property_count: 1
  slug: createvariableoption
- name: CreateWikiPageOptions
  property_count: 3
  slug: createwikipageoptions
- name: Cron
  property_count: 5
  slug: cron
- name: DeleteEmailOption
  property_count: 1
  slug: deleteemailoption
- name: DeleteFileOptions
  property_count: 9
  slug: deletefileoptions
- name: DeleteLabelsOption
  property_count: 1
  slug: deletelabelsoption
- name: DeployKey
  property_count: 9
  slug: deploykey
- name: DismissPullReviewOptions
  property_count: 2
  slug: dismisspullreviewoptions
- name: DispatchWorkflowOption
  property_count: 3
  slug: dispatchworkflowoption
- name: DispatchWorkflowRun
  property_count: 3
  slug: dispatchworkflowrun
- name: Duration
  property_count: 0
  slug: duration
- name: EditAttachmentOptions
  property_count: 2
  slug: editattachmentoptions
- name: EditBranchProtectionOption
  property_count: 23
  slug: editbranchprotectionoption
- name: EditDeadlineOption
  property_count: 1
  slug: editdeadlineoption
- name: EditGitHookOption
  property_count: 1
  slug: editgithookoption
- name: EditHookOption
  property_count: 5
  slug: edithookoption
- name: EditIssueCommentOption
  property_count: 2
  slug: editissuecommentoption
- name: EditIssueOption
  property_count: 10
  slug: editissueoption
- name: EditLabelOption
  property_count: 5
  slug: editlabeloption
- name: EditMilestoneOption
  property_count: 4
  slug: editmilestoneoption
- name: EditOrgOption
  property_count: 7
  slug: editorgoption
- name: EditPullRequestOption
  property_count: 11
  slug: editpullrequestoption
- name: EditQuotaRuleOptions
  property_count: 2
  slug: editquotaruleoptions
- name: EditReactionOption
  property_count: 1
  slug: editreactionoption
- name: EditReleaseOption
  property_count: 7
  slug: editreleaseoption
- name: EditRepoOption
  property_count: 34
  slug: editrepooption
- name: EditTagProtectionOption
  property_count: 3
  slug: edittagprotectionoption
- name: EditTeamOption
  property_count: 7
  slug: editteamoption
- name: EditUserOption
  property_count: 20
  slug: edituseroption
- name: Email
  property_count: 5
  slug: email
- name: ExternalTracker
  property_count: 4
  slug: externaltracker
- name: ExternalWiki
  property_count: 1
  slug: externalwiki
- name: FileCommitResponse contains information generated from a Git commit for a repo's file.
  property_count: 9
  slug: filecommitresponse
- name: FileDeleteResponse
  property_count: 3
  slug: filedeleteresponse
- name: FileLinksResponse
  property_count: 3
  slug: filelinksresponse
- name: FileResponse
  property_count: 3
  slug: fileresponse
- name: FilesResponse
  property_count: 3
  slug: filesresponse
- name: ForgeLike
  property_count: 0
  slug: forgelike
- name: ForgeOutbox
  property_count: 0
  slug: forgeoutbox
- name: GeneralAPISettings
  property_count: 4
  slug: generalapisettings
- name: GeneralAttachmentSettings
  property_count: 4
  slug: generalattachmentsettings
- name: GeneralRepoSettings
  property_count: 7
  slug: generalreposettings
- name: GeneralUISettings
  property_count: 3
  slug: generaluisettings
- name: GenerateRepoOption
  property_count: 12
  slug: generaterepooption
- name: GitBlob
  property_count: 5
  slug: gitblob
- name: GitEntry
  property_count: 6
  slug: gitentry
- name: GitHook
  property_count: 3
  slug: githook
- name: GitignoreTemplateInfo
  property_count: 2
  slug: gitignoretemplateinfo
- name: GitObject represents a Git object.
  property_count: 3
  slug: gitobject
- name: GitTreeResponse
  property_count: 6
  slug: gittreeresponse
- name: GPGKey
  property_count: 13
  slug: gpgkey
- name: GPGKeyEmail
  property_count: 2
  slug: gpgkeyemail
- name: Hook
  property_count: 12
  slug: hook
- name: Identity
  property_count: 2
  slug: identity
- name: InternalTracker
  property_count: 3
  slug: internaltracker
- name: Issue
  property_count: 25
  slug: issue
- name: IssueConfig
  property_count: 2
  slug: issueconfig
- name: IssueConfigContactLink
  property_count: 3
  slug: issueconfigcontactlink
- name: IssueConfigValidation
  property_count: 2
  slug: issueconfigvalidation
- name: IssueDeadline
  property_count: 1
  slug: issuedeadline
- name: IssueFormField
  property_count: 5
  slug: issueformfield
- name: IssueFormFieldType defines issue form field type, can be "markdown", "textarea", "input", "dropdown" or "checkboxes"
  property_count: 0
  slug: issueformfieldtype
- name: IssueFormFieldVisible
  property_count: 0
  slug: issueformfieldvisible
- name: IssueLabelsOption
  property_count: 2
  slug: issuelabelsoption
- name: IssueMeta
  property_count: 3
  slug: issuemeta
- name: IssueTemplate
  property_count: 8
  slug: issuetemplate
- name: IssueTemplateLabels
  property_count: 0
  slug: issuetemplatelabels
- name: Label
  property_count: 7
  slug: label
- name: LabelTemplate
  property_count: 4
  slug: labeltemplate
- name: LicensesTemplateListEntry
  property_count: 3
  slug: licensestemplatelistentry
- name: LicenseTemplateInfo
  property_count: 5
  slug: licensetemplateinfo
- name: ListActionRunResponse
  property_count: 2
  slug: listactionrunresponse
- name: MarkdownOption
  property_count: 4
  slug: markdownoption
- name: MarkupOption
  property_count: 6
  slug: markupoption
- name: MergePullRequestOption
  property_count: 8
  slug: mergepullrequestoption
- name: MigrateRepoOptions
  property_count: 20
  slug: migraterepooptions
- name: Milestone
  property_count: 10
  slug: milestone
- name: NewIssuePinsAllowed
  property_count: 2
  slug: newissuepinsallowed
- name: NodeInfo
  property_count: 7
  slug: nodeinfo
- name: NodeInfoServices
  property_count: 2
  slug: nodeinfoservices
- name: NodeInfoSoftware
  property_count: 4
  slug: nodeinfosoftware
- name: NodeInfoUsage
  property_count: 3
  slug: nodeinfousage
- name: NodeInfoUsageUsers
  property_count: 3
  slug: nodeinfousageusers
- name: Note
  property_count: 2
  slug: note
- name: NoteOptions
  property_count: 1
  slug: noteoptions
- name: NotificationCount
  property_count: 1
  slug: notificationcount
- name: NotificationSubject
  property_count: 7
  slug: notificationsubject
- name: NotificationThread
  property_count: 7
  slug: notificationthread
- name: NotifySubjectType
  property_count: 0
  slug: notifysubjecttype
- name: OAuth2Application represents an OAuth2 application.
  property_count: 7
  slug: oauth2application
- name: Organization
  property_count: 12
  slug: organization
- name: OrganizationPermissions
  property_count: 5
  slug: organizationpermissions
- name: Package
  property_count: 9
  slug: package
- name: PackageFile
  property_count: 7
  slug: packagefile
- name: PayloadCommit
  property_count: 10
  slug: payloadcommit
- name: PayloadCommitVerification
  property_count: 5
  slug: payloadcommitverification
- name: PayloadUser
  property_count: 3
  slug: payloaduser
- name: Permission
  property_count: 3
  slug: permission
- name: PRBranchInfo
  property_count: 5
  slug: prbranchinfo
- name: PublicKey
  property_count: 11
  slug: publickey
- name: PullRequest
  property_count: 38
  slug: pullrequest
- name: PullRequestMeta
  property_count: 4
  slug: pullrequestmeta
- name: PullReview
  property_count: 14
  slug: pullreview
- name: PullReviewComment
  property_count: 16
  slug: pullreviewcomment
- name: PullReviewRequestOptions
  property_count: 2
  slug: pullreviewrequestoptions
- name: PushMirror
  property_count: 10
  slug: pushmirror
- name: QuotaGroup
  property_count: 2
  slug: quotagroup
- name: QuotaGroupList
  property_count: 0
  slug: quotagrouplist
- name: QuotaInfo
  property_count: 2
  slug: quotainfo
- name: QuotaRuleInfo
  property_count: 3
  slug: quotaruleinfo
- name: QuotaUsed
  property_count: 1
  slug: quotaused
- name: QuotaUsedArtifact
  property_count: 3
  slug: quotausedartifact
- name: QuotaUsedArtifactList
  property_count: 0
  slug: quotausedartifactlist
- name: QuotaUsedAttachment
  property_count: 4
  slug: quotausedattachment
- name: QuotaUsedAttachmentList
  property_count: 0
  slug: quotausedattachmentlist
- name: QuotaUsedPackage
  property_count: 5
  slug: quotausedpackage
- name: QuotaUsedPackageList
  property_count: 0
  slug: quotausedpackagelist
- name: QuotaUsedSize
  property_count: 3
  slug: quotausedsize
- name: QuotaUsedSizeAssets
  property_count: 3
  slug: quotausedsizeassets
- name: QuotaUsedSizeAssetsAttachments
  property_count: 2
  slug: quotausedsizeassetsattachments
- name: QuotaUsedSizeAssetsPackages
  property_count: 1
  slug: quotausedsizeassetspackages
- name: QuotaUsedSizeGit
  property_count: 1
  slug: quotausedsizegit
- name: QuotaUsedSizeRepos
  property_count: 2
  slug: quotausedsizerepos
- name: Reaction
  property_count: 3
  slug: reaction
- name: Reference represents a Git reference.
  property_count: 3
  slug: reference
- name: RegisterRunnerOptions declares the accepted options for registering runners.
  property_count: 3
  slug: registerrunneroptions
- name: RegisterRunnerResponse contains the details of the just registered runner.
  property_count: 3
  slug: registerrunnerresponse
- name: RegistrationToken
  property_count: 1
  slug: registrationtoken
- name: Release
  property_count: 18
  slug: release
- name: RenameOrgOption
  property_count: 1
  slug: renameorgoption
- name: RenameUserOption
  property_count: 1
  slug: renameuseroption
- name: ReplaceFlagsOption
  property_count: 1
  slug: replaceflagsoption
- name: RepoCollaboratorPermission
  property_count: 3
  slug: repocollaboratorpermission
- name: RepoCommit contains information of a commit in the context of a repository.
  property_count: 6
  slug: repocommit
- name: Repository
  property_count: 66
  slug: repository
- name: RepositoryMeta
  property_count: 4
  slug: repositorymeta
- name: RepoTargetOption
  property_count: 2
  slug: repotargetoption
- name: RepoTopicOptions
  property_count: 1
  slug: repotopicoptions
- name: RepoTransfer
  property_count: 3
  slug: repotransfer
- name: ReviewStateType
  property_count: 0
  slug: reviewstatetype
- name: SearchResults
  property_count: 2
  slug: searchresults
- name: Secret
  property_count: 2
  slug: secret
- name: ServerVersion
  property_count: 1
  slug: serverversion
- name: SetUserQuotaGroupsOptions
  property_count: 1
  slug: setuserquotagroupsoptions
- name: StateType
  property_count: 0
  slug: statetype
- name: StopWatch
  property_count: 7
  slug: stopwatch
- name: SubmitPullReviewOptions
  property_count: 2
  slug: submitpullreviewoptions
- name: SyncForkInfo
  property_count: 4
  slug: syncforkinfo
- name: Tag
  property_count: 7
  slug: tag
- name: TagArchiveDownloadCount
  property_count: 2
  slug: tagarchivedownloadcount
- name: TagProtection
  property_count: 6
  slug: tagprotection
- name: Team
  property_count: 9
  slug: team
- name: TimelineComment
  property_count: 29
  slug: timelinecomment
- name: TimeStamp
  property_count: 0
  slug: timestamp
- name: TopicName
  property_count: 1
  slug: topicname
- name: TopicResponse
  property_count: 5
  slug: topicresponse
- name: TrackedTime
  property_count: 7
  slug: trackedtime
- name: TransferRepoOption
  property_count: 2
  slug: transferrepooption
- name: UpdateBranchRepoOption
  property_count: 1
  slug: updatebranchrepooption
- name: UpdateFileOptions
  property_count: 11
  slug: updatefileoptions
- name: UpdateRepoAvatarOption
  property_count: 1
  slug: updaterepoavataroption
- name: UpdateUserAvatarOption
  property_count: 1
  slug: updateuseravataroption
- name: UpdateVariableOption defines the properties of the variable to update.
  property_count: 2
  slug: updatevariableoption
- name: User
  property_count: 23
  slug: user
- name: UserHeatmapData
  property_count: 2
  slug: userheatmapdata
- name: UserSettings
  property_count: 12
  slug: usersettings
- name: UserSettingsOptions
  property_count: 12
  slug: usersettingsoptions
- name: VerifyGPGKeyOption
  property_count: 2
  slug: verifygpgkeyoption
- name: WatchInfo
  property_count: 6
  slug: watchinfo
- name: WikiCommit
  property_count: 4
  slug: wikicommit
- name: WikiCommitList
  property_count: 2
  slug: wikicommitlist
- name: WikiPage
  property_count: 8
  slug: wikipage
- name: WikiPageMetaData
  property_count: 4
  slug: wikipagemetadata
layout: provider
modified: '2026-06-13'
name: Forgejo
nav: Providers
network: true
overview: 'Forgejo publishes 10 APIs on the [APIs.io](https://apis.io/) network, including activitypub API, admin API, issue API, and 7 more. Tagged areas include Git, Source Code Management, Self-Hosted, DevOps, and CI/CD.


  The Forgejo catalog on APIs.io includes 1 Spectral governance ruleset.


  Forgejo''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Forgejo Plans Pricing
  plan_count: 2
  slug: forgejo-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 0
  name: Forgejo Rate Limits
  slug: forgejo-rate-limits
rules:
- name: Forgejo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: forgejo-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.5
  delta: -5.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 32.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/forgejo/refs/heads/main/screenshots/forgejo-2026-06-20T181426.png
security:
- kind: authentication
  name: Forgejo Authentication
  slug: forgejo-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Forgejo Domain Security
  slug: forgejo-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Forgejo Vulnerability Disclosure
  slug: forgejo-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: forgejo
tags:
- Git
- Source Code Management
- Self-Hosted
- DevOps
- CI/CD
- Open Source
- Forge
- Repositories
- Issues
- Pull Requests
website: https://forgejo.org
---

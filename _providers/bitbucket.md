---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.2
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 166
  human_in_the_loop: 4
  name: Bitbucket Agentic Access
  operation_count: 361
  slug: bitbucket-agentic-access
  summary_line: 361 operations · 166 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: The addon resource is intended to use used by Bitbucket Cloud Connect Apps, and only supports JWT authentication.
  name: Bitbucket Addon API
  phrasing_intents:
  - id: deleteAddon
    intent: Uninstall a Connect app
    question: How can a Connect app remove its own installation for a user?
  - id: putAddon
    intent: Update an installed Connect app
    question: How does a Bitbucket Connect app update its own installation?
  - id: getAddonLinkers
    intent: List an app's linkers
    question: Which linkers has my Connect app registered?
  - id: getAddonLinkersByLinkerKey
    intent: Get one linker of an app
    question: What does a single app linker look like, including its regex?
  - id: deleteAddonLinkersByLinkerKeyValues
    intent: Delete all values of a linker
    question: How do I clear every value from a linker at once?
  - id: getAddonLinkersByLinkerKeyValues
    intent: List the values of a linker
    question: What values currently feed into my linker's regular expression?
  - id: postAddonLinkersByLinkerKeyValues
    intent: Add a value to a linker
    question: How do I add one more value to my app's linker?
  - id: putAddonLinkersByLinkerKeyValues
    intent: Bulk replace a linker's values
    question: Can I replace all of a linker's values in one call?
  phrasing_ops: 10
  slug: bitbucket-addon-api
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: Repository owners and administrators can set branch management rules on a repository that control what can be pushed by whom. Through these rules, you can enforce a project or team workflow. For examp
  name: Bitbucket Branch restrictions API
  phrasing_intents:
  - id: getRepositoriesByWorkspaceByRepoSlugBranchRestrictions
    intent: List a repository's branch restrictions
    question: Which branch protection rules are set on my Bitbucket repo?
  - id: postRepositoriesByWorkspaceByRepoSlugBranchRestrictions
    intent: Create a branch restriction rule
    question: How do I stop people force-pushing to main?
  - id: deleteRepositoriesByWorkspaceByRepoSlugBranchRestrictionsById
    intent: Delete a branch restriction rule
    question: How do I remove a branch protection rule?
  - id: getRepositoriesByWorkspaceByRepoSlugBranchRestrictionsById
    intent: Get a branch restriction rule
    question: Can I look up a single branch restriction by its id?
  - id: putRepositoriesByWorkspaceByRepoSlugBranchRestrictionsById
    intent: Update a branch restriction rule
    question: How do I change the pattern an existing branch restriction applies to?
  phrasing_ops: 5
  slug: bitbucket-branch-restrictions-api
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: The branching model resource is used to modify the branching model for a repository. You can use the branching model to define a branch based workflow for your repositories. When you map your workflow
  name: Bitbucket Branching model API
  phrasing_intents:
  - id: getRepositoriesByWorkspaceByRepoSlugBranchingModel
    intent: Get a repository's branching model
    question: What are the development and production branches for this repo?
  - id: getRepositoriesByWorkspaceByRepoSlugBranchingModelSettings
    intent: Get a repository's branching model config
    question: How is the branching model configured for my repo, including disabled branch types?
  - id: putRepositoriesByWorkspaceByRepoSlugBranchingModelSettings
    intent: Update a repository's branching model config
    question: How do I change the development branch for my repository?
  - id: getRepositoriesByWorkspaceByRepoSlugEffectiveBranchingModel
    intent: Get a repo's effective branching model
    question: Which branching model is actually in effect for my repo, repo or project level?
  - id: getWorkspacesByWorkspaceProjectsByProjectKeyBranchingModel
    intent: Get a project's branching model
    question: What branching model is set at the project level?
  - id: getWorkspacesByWorkspaceProjectsByProjectKeyBranchingModelSettings
    intent: Get a project's branching model config
    question: How is the branching model configured for a whole project?
  - id: putWorkspacesByWorkspaceProjectsByProjectKeyBranchingModelSettings
    intent: Update a project's branching model config
    question: How do I set a default branching model for every repo in a project?
  phrasing_ops: 7
  slug: bitbucket-branching-model-api
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: Commit statuses provide a way to tag commits with meta data, like automated build results.
  name: Bitbucket Commit statuses API
  phrasing_intents:
  - id: getRepositoriesByWorkspaceByRepoSlugCommitByCommitStatuses
    intent: List build statuses for a commit
    question: Did the builds pass on this commit?
  - id: postRepositoriesByWorkspaceByRepoSlugCommitByCommitStatusesBuild
    intent: Report a build status on a commit
    question: How does my CI server post a build result to a Bitbucket commit?
  - id: getRepositoriesByWorkspaceByRepoSlugCommitByCommitStatusesBuildByKey
    intent: Get one build status on a commit
    question: What is the state of one particular build on a commit?
  - id: putRepositoriesByWorkspaceByRepoSlugCommitByCommitStatusesBuildByKey
    intent: Update a build status on a commit
    question: How do I flip an existing build status from in progress to successful?
  - id: getRepositoriesByWorkspaceByRepoSlugPullrequestsByPullRequestIdStatuses
    intent: List build statuses for a pull request
    question: Are all the checks green on this pull request?
  phrasing_ops: 5
  slug: bitbucket-commit-statuses-api
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: These are the repository's commits. They are paginated and returned in reverse chronological order, similar to the output of git log.
  name: Bitbucket Commits API
  phrasing_intents:
  - id: getRepositoriesByWorkspaceByRepoSlugCommitByCommit
    intent: Get a commit
    question: Who authored this commit and what was its message?
  - id: deleteRepositoriesByWorkspaceByRepoSlugCommitByCommitApprove
    intent: Withdraw my approval of a commit
    question: How do I take back my approval on a commit?
  - id: postRepositoriesByWorkspaceByRepoSlugCommitByCommitApprove
    intent: Approve a commit
    question: Can I sign off on an individual commit?
  - id: getRepositoriesByWorkspaceByRepoSlugCommitByCommitComments
    intent: List comments on a commit
    question: What have people said about this commit, inline and general?
  - id: postRepositoriesByWorkspaceByRepoSlugCommitByCommitComments
    intent: Comment on a commit
    question: How do I leave a comment on a commit?
  - id: deleteRepositoriesByWorkspaceByRepoSlugCommitByCommitCommentsByCommentId
    intent: Delete a commit comment
    question: How do I delete a comment I left on a commit?
  - id: getRepositoriesByWorkspaceByRepoSlugCommitByCommitCommentsByCommentId
    intent: Get a commit comment
    question: Can I fetch one comment on a commit by id?
  - id: putRepositoriesByWorkspaceByRepoSlugCommitByCommitCommentsByCommentId
    intent: Edit a commit comment
    question: How do I fix a typo in a comment I left on a commit?
  phrasing_ops: 25
  slug: bitbucket-commits-api
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: Teams are deploying code faster than ever, thanks to continuous delivery practices and tools like Bitbucket Pipelines. Bitbucket Deployments gives teams visibility into their deployment environments a
  name: Bitbucket Deployments API
  phrasing_intents:
  - id: getRepositoriesByWorkspaceByRepoSlugDeployKeys
    intent: List a repository's deploy keys
    question: Which read-only access keys are installed on this repo?
  - id: postRepositoriesByWorkspaceByRepoSlugDeployKeys
    intent: Add a deploy key to a repository
    question: How do I give a build server SSH access to a single repo?
  - id: deleteRepositoriesByWorkspaceByRepoSlugDeployKeysByKeyId
    intent: Remove a repository deploy key
    question: How do I revoke a deploy key from one repo?
  - id: getRepositoriesByWorkspaceByRepoSlugDeployKeysByKeyId
    intent: Get a repository deploy key
    question: What label and comment does a specific repo deploy key have?
  - id: putRepositoriesByWorkspaceByRepoSlugDeployKeysByKeyId
    intent: Relabel a repository deploy key
    question: How do I rename the label on an existing repo deploy key?
  - id: getDeploymentsForRepository
    intent: List deployments in a repository
    question: What has been deployed from this repository recently?
  - id: getDeploymentForRepository
    intent: Get a deployment
    question: What's the state of one specific deployment?
  - id: getEnvironmentsForRepository
    intent: List deployment environments
    question: Which deployment environments are set up for this repo?
  phrasing_ops: 16
  slug: bitbucket-deployments-api
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: Access the list of download links associated with the repository.
  name: Bitbucket Downloads API
  phrasing_intents:
  - id: getRepositoriesByWorkspaceByRepoSlugDownloads
    intent: List a repository's download artifacts
    question: What files are published in my repo's Downloads section?
  - id: postRepositoriesByWorkspaceByRepoSlugDownloads
    intent: Upload a download artifact
    question: How do I upload a release binary to my repo's Downloads?
  - id: deleteRepositoriesByWorkspaceByRepoSlugDownloadsByFilename
    intent: Delete a download artifact
    question: How do I remove an old file from Downloads?
  - id: getRepositoriesByWorkspaceByRepoSlugDownloadsByFilename
    intent: Download a repository artifact file
    question: How do I fetch the contents of a file from a repo's Downloads?
  phrasing_ops: 4
  slug: bitbucket-downloads-api
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: The GPG resource allows you to manage GPG keys.
  name: Bitbucket GPG API
  phrasing_intents:
  - id: getUsersBySelectedUserGpgKeys
    intent: List a user's GPG keys
    question: Which GPG keys are registered on my account for signing commits?
  - id: postUsersBySelectedUserGpgKeys
    intent: Add a GPG key to a user
    question: How do I add a GPG key so my signed commits show as verified?
  - id: deleteUsersBySelectedUserGpgKeysByFingerprint
    intent: Delete a GPG key
    question: How do I remove a compromised GPG key from my account?
  - id: getUsersBySelectedUserGpgKeysByFingerprint
    intent: Get a GPG key by fingerprint
    question: Can I look up one GPG key by its fingerprint?
  phrasing_ops: 4
  slug: bitbucket-gpg-api
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: The issue resources provide functionality for getting information on issues in an issue tracker, creating new issues, updating them and deleting them. You can access public issues without authenticati
  name: Bitbucket Issue tracker API
  phrasing_intents:
  - id: getRepositoriesByWorkspaceByRepoSlugComponents
    intent: List issue tracker components
    question: What components can I file issues against in a repository's tracker?
  - id: getRepositoriesByWorkspaceByRepoSlugComponentsByComponentId
    intent: Get an issue tracker component
    question: What is the name of the issue component with a given id?
  - id: getRepositoriesByWorkspaceByRepoSlugIssues
    intent: List a repository's issues
    question: What issues are filed in a Bitbucket repository's tracker?
  - id: postRepositoriesByWorkspaceByRepoSlugIssues
    intent: File a new issue
    question: How do I report a new bug in a repository's issue tracker?
  - id: postRepositoriesByWorkspaceByRepoSlugIssuesExport
    intent: Start an export of a repo's issues
    question: How do I back up every issue in a repository to a zip archive?
  - id: getRepositoriesByWorkspaceByRepoSlugIssuesExport{repoName}Issues{taskId}Zip
    intent: Check an issue export and download the zip
    question: Has my issue export finished, and where do I get the zip file?
  - id: getRepositoriesByWorkspaceByRepoSlugIssuesImport
    intent: Check the status of an issue import
    question: Is the issue import I started still running or has it completed?
  - id: postRepositoriesByWorkspaceByRepoSlugIssuesImport
    intent: Import issues from a zip, replacing existing ones
    question: How do I load an issue archive zip into a repository's tracker?
  phrasing_ops: 33
  slug: bitbucket-issue-tracker-api
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: Bitbucket Pipelines brings continuous delivery to Bitbucket Cloud, empowering teams with full branching to deployment visibility and faster feedback loops.
  name: Bitbucket Pipelines API
  phrasing_intents:
  - id: getDeploymentVariables
    intent: List variables for a deployment environment
    question: Which variables are set on my staging deployment environment?
  - id: createDeploymentVariable
    intent: Add a variable to a deployment environment
    question: How do I add a secret just for my production deployment environment?
  - id: updateDeploymentVariable
    intent: Update a deployment environment variable
    question: How do I change the value of an existing variable on a deployment environment?
  - id: deleteDeploymentVariable
    intent: Remove a variable from a deployment environment
    question: How do I remove a variable that's only defined on one deployment environment?
  - id: getPipelinesForRepository
    intent: List pipeline runs in a repository
    question: Which pipelines have run on my main branch recently?
  - id: createPipelineForRepository
    intent: Run a pipeline
    question: How do I trigger a Bitbucket pipeline run from the API?
  - id: getRepositoryPipelineCaches
    intent: List a repository's pipeline caches
    question: What dependency caches are my pipelines storing for this repo?
  - id: deleteRepositoryPipelineCaches
    intent: Clear pipeline caches by name
    question: How do I wipe every version of the node cache for my pipelines?
  phrasing_ops: 68
  slug: bitbucket-pipelines-api
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: Bitbucket Cloud projects make it easier for teams to focus on a goal, product, or process by organizing their repositories.
  name: Bitbucket Projects API
  phrasing_intents:
  - id: postWorkspacesByWorkspaceProjects
    intent: Create a project in a workspace
    question: How do I create a new project to group repositories?
  - id: deleteWorkspacesByWorkspaceProjectsByProjectKey
    intent: Delete a project
    question: How do I delete an empty project?
  - id: getWorkspacesByWorkspaceProjectsByProjectKey
    intent: Get a project
    question: What are the details of a Bitbucket project?
  - id: putWorkspacesByWorkspaceProjectsByProjectKey
    intent: Update or create a project by key
    question: How do I rename an existing project?
  - id: getWorkspacesByWorkspaceProjectsByProjectKeyDefaultReviewers
    intent: List a project's default reviewers
    question: Who gets added automatically as a reviewer on PRs across a project?
  - id: deleteWorkspacesByWorkspaceProjectsByProjectKeyDefaultReviewersBySelectedUser
    intent: Remove a project default reviewer
    question: How do I stop someone being auto-added to PRs across a project?
  - id: getWorkspacesByWorkspaceProjectsByProjectKeyDefaultReviewersBySelectedUser
    intent: Check a project default reviewer
    question: Is a particular user a default reviewer for this project?
  - id: putWorkspacesByWorkspaceProjectsByProjectKeyDefaultReviewersBySelectedUser
    intent: Add a project default reviewer
    question: How do I make someone a default reviewer for every repo in a project?
  phrasing_ops: 16
  slug: bitbucket-projects-api
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: The properties API from Bitbucket — 4 operation(s) for properties.
  name: Bitbucket Properties API
  phrasing_intents:
  - id: updateCommitHostedPropertyValue
    intent: Store an app property on a commit
    question: How can my app save its own metadata against a commit?
  - id: deleteCommitHostedPropertyValue
    intent: Delete an app property from a commit
    question: How do I remove data my app stored on a commit?
  - id: getCommitHostedPropertyValue
    intent: Read an app property stored on a commit
    question: How does my Connect app read data it saved against a specific commit?
  - id: updateRepositoryHostedPropertyValue
    intent: Store an app property on a repository
    question: How can my app persist per-repository configuration in Bitbucket?
  - id: deleteRepositoryHostedPropertyValue
    intent: Delete an app property from a repository
    question: How do I remove an application property my app stored on a repo?
  - id: getRepositoryHostedPropertyValue
    intent: Read an app property stored on a repository
    question: How does my app read settings it saved at the repository level?
  - id: updatePullRequestHostedPropertyValue
    intent: Store an app property on a pull request
    question: How can my app attach its own state to a pull request?
  - id: deletePullRequestHostedPropertyValue
    intent: Delete an app property from a pull request
    question: How do I remove data my app saved on a pull request?
  phrasing_ops: 12
  slug: bitbucket-properties-api
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: The refs resource allows you access branches and tags in a repository. By default, results will be in the order the underlying source control system returns them and identical to the ordering one sees
  name: Bitbucket Refs API
  phrasing_intents:
  - id: getRepositoriesByWorkspaceByRepoSlugRefs
    intent: List branches and tags together
    question: Can I see every branch and tag in a repo in one list?
  - id: getRepositoriesByWorkspaceByRepoSlugRefsBranches
    intent: List open branches
    question: Which branches are open in my Bitbucket repo?
  - id: postRepositoriesByWorkspaceByRepoSlugRefsBranches
    intent: Create a branch
    question: How do I create a new branch from a commit through the API?
  - id: deleteRepositoriesByWorkspaceByRepoSlugRefsBranchesByName
    intent: Delete a branch
    question: How do I delete a merged branch?
  - id: getRepositoriesByWorkspaceByRepoSlugRefsBranchesByName
    intent: Get a branch
    question: What commit is a branch pointing at right now?
  - id: getRepositoriesByWorkspaceByRepoSlugRefsTags
    intent: List tags
    question: Which release tags exist in my repo?
  - id: postRepositoriesByWorkspaceByRepoSlugRefsTags
    intent: Create an annotated tag
    question: How do I tag a release commit?
  - id: deleteRepositoriesByWorkspaceByRepoSlugRefsTagsByName
    intent: Delete a tag
    question: How do I remove a tag I created by mistake?
  phrasing_ops: 9
  slug: bitbucket-refs-api
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: Code insights provides reports, annotations, and metrics to help you and your team improve code quality in pull requests throughout the code review process. Some of the available code insights are sta
  name: Bitbucket Reports API
  phrasing_intents:
  - id: getReportsForCommit
    intent: List reports attached to a commit
    question: What test, coverage or scan reports exist for a given commit?
  - id: createOrUpdateReport
    intent: Create or update a code insight report
    question: How can my CI tool publish coverage results as a report on a commit?
  - id: getReport
    intent: Retrieve a single code insight report
    question: Did a particular code insight report pass or fail?
  - id: deleteReport
    intent: Remove a code insight report
    question: How can I delete an outdated code insight report from a commit?
  - id: getAnnotationsForReport
    intent: List the findings in a code insight report
    question: What issues did a code insight report flag, line by line?
  - id: bulkCreateOrUpdateAnnotations
    intent: Bulk upload findings to a code insight report
    question: How can I send all my linter findings to a report in a single request?
  - id: getAnnotation
    intent: Retrieve a single report finding
    question: What severity and file location does one report finding have?
  - id: createOrUpdateAnnotation
    intent: Upsert one finding on a code insight report
    question: How can I mark a single vulnerability on a specific file and line in a report?
  phrasing_ops: 9
  slug: bitbucket-reports-api
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: A Git repository is a virtual storage of your project. It allows you to save versions of your code, which you can access when needed. The repo resource allows you to access public repos, or repos that
  name: Bitbucket Repositories API
  phrasing_intents:
  - id: getRepositories
    intent: List all public repositories (deprecated)
    question: Can I browse every public repository on Bitbucket, not just one workspace's?
  - id: getRepositoriesByWorkspace
    intent: List repositories in a workspace
    question: What repositories does a workspace own?
  - id: deleteRepositoriesByWorkspaceByRepoSlug
    intent: Delete a repository
    question: How do I permanently delete a repository? Do its forks survive?
  - id: getRepositoriesByWorkspaceByRepoSlug
    intent: Get a repository
    question: What is a repository's main branch, language and privacy setting?
  - id: postRepositoriesByWorkspaceByRepoSlug
    intent: Create a repository
    question: How do I create a new git repository in a workspace?
  - id: putRepositoriesByWorkspaceByRepoSlug
    intent: Update a repository's settings
    question: Can I rename a repository or change its description through the API?
  - id: getRepositoriesByWorkspaceByRepoSlugFilehistoryByCommitByPath
    intent: List commits that changed a file
    question: Which commits modified a specific file, newest first?
  - id: getRepositoriesByWorkspaceByRepoSlugForks
    intent: List forks of a repository
    question: Who has forked a repository?
  phrasing_ops: 30
  slug: bitbucket-repositories-api
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: The Search API from Bitbucket — 3 operation(s) for search.
  name: Bitbucket Search API
  phrasing_intents:
  - id: searchTeam
    intent: Search code across a team's repositories
    question: How do I find where a function is used across all of my team's repos?
  - id: searchAccount
    intent: Search code in a user's repositories
    question: How can I search the code in one user's personal repositories?
  - id: searchWorkspace
    intent: Search code across a workspace
    question: Where in my workspace is a particular config key referenced?
  phrasing_ops: 3
  slug: bitbucket-search-api
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: Snippets allow you share code segments or files with yourself, members of your workspace, or the world. Like pull requests, repositories and workspaces, the full set of snippets is defined by what the
  name: Bitbucket Snippets API
  phrasing_intents:
  - id: getSnippets
    intent: List snippets I can see (deprecated)
    question: Which code snippets can I access across every workspace?
  - id: postSnippets
    intent: Create a snippet under my account
    question: How do I share a quick code snippet from my own account?
  - id: getSnippetsByWorkspace
    intent: List snippets owned by a workspace
    question: What snippets does a particular workspace own?
  - id: postSnippetsByWorkspace
    intent: Create a snippet in a workspace
    question: How do I create a snippet that belongs to a team workspace instead of me?
  - id: deleteSnippetsByWorkspaceByEncodedId
    intent: Delete a snippet
    question: How do I permanently delete a snippet?
  - id: getSnippetsByWorkspaceByEncodedId
    intent: Get a snippet
    question: What files and title does a specific snippet have at its latest version?
  - id: putSnippetsByWorkspaceByEncodedId
    intent: Update a snippet
    question: How do I edit the files or title of an existing snippet?
  - id: getSnippetsByWorkspaceByEncodedIdComments
    intent: List comments on a snippet
    question: What have people said in the comments on a snippet?
  phrasing_ops: 25
  slug: bitbucket-snippets-api
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: Browse the source code in the repository and create new commits by uploading.
  name: Bitbucket Source API
  phrasing_intents:
  - id: getRepositoriesByWorkspaceByRepoSlugFilehistoryByCommitByPath
    intent: List commits that changed a file
    question: Who changed this file and when?
  - id: getRepositoriesByWorkspaceByRepoSlugSrc
    intent: Browse the main branch root directory
    question: What files are at the top level of my repo's main branch?
  - id: postRepositoriesByWorkspaceByRepoSlugSrc
    intent: Commit files by uploading them
    question: Can I make a commit by uploading a file, without git?
  - id: getRepositoriesByWorkspaceByRepoSlugSrcByCommitByPath
    intent: Read a file or directory at a revision
    question: What did this file look like at an older commit?
  phrasing_ops: 4
  slug: bitbucket-source-api
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: The SSH resource allows you to manage SSH keys.
  name: Bitbucket SSH API
  phrasing_intents:
  - id: getUsersBySelectedUserSshKeys
    intent: List a user's SSH keys
    question: Which SSH keys are on my Bitbucket account?
  - id: postUsersBySelectedUserSshKeys
    intent: Add an SSH key to a user
    question: How do I add a new SSH key to my account?
  - id: deleteUsersBySelectedUserSshKeysByKeyId
    intent: Delete an SSH key
    question: How do I revoke an SSH key from my account?
  - id: getUsersBySelectedUserSshKeysByKeyId
    intent: Get an SSH key
    question: Can I look up one SSH key by its id?
  - id: putUsersBySelectedUserSshKeysByKeyId
    intent: Update an SSH key's comment
    question: How do I change the label on an existing SSH key?
  phrasing_ops: 5
  slug: bitbucket-ssh-api
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: The users resource allows you to access public information associated with a user account. Most resources in the users endpoint have been deprecated in favor of workspaces.
  name: Bitbucket Users API
  phrasing_intents:
  - id: getUser
    intent: Get the current user
    question: Who am I logged in as on Bitbucket?
  - id: getUserEmails
    intent: List my email addresses
    question: What email addresses are on my account, confirmed or not?
  - id: getUserEmailsByEmail
    intent: Check one of my email addresses
    question: Is this email address confirmed on my account?
  - id: getUsersBySelectedUser
    intent: Get a user's public profile
    question: What public information can I see about another Bitbucket user?
  phrasing_ops: 4
  slug: bitbucket-users-api
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: 'Webhooks provide a way to configure Bitbucket Cloud to make requests to your server (or another external service) whenever certain events occur in Bitbucket Cloud. A webhook consists of: * A subject -'
  name: Bitbucket Webhooks API
  phrasing_intents:
  - id: getHookEvents
    intent: List webhook subject types
    question: What kinds of things can I attach webhooks to?
  - id: getHookEventsBySubjectType
    intent: List webhook events for a subject type
    question: Which events can a repository webhook subscribe to?
  - id: getRepositoriesByWorkspaceByRepoSlugHooks
    intent: List a repository's webhooks
    question: What webhooks are installed on this repository?
  - id: postRepositoriesByWorkspaceByRepoSlugHooks
    intent: Create a repository webhook
    question: How do I get notified when someone pushes to one repo?
  - id: deleteRepositoriesByWorkspaceByRepoSlugHooksByUid
    intent: Delete a repository webhook
    question: How do I remove a webhook from one repository?
  - id: getRepositoriesByWorkspaceByRepoSlugHooksByUid
    intent: Get a repository webhook
    question: Which events does a particular repo webhook fire on?
  - id: putRepositoriesByWorkspaceByRepoSlugHooksByUid
    intent: Update a repository webhook
    question: How do I change the URL of a repo webhook?
  - id: getWorkspacesByWorkspaceHooks
    intent: List a workspace's webhooks
    question: Which webhooks fire for every repo in my workspace?
  phrasing_ops: 12
  slug: bitbucket-webhooks-api
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: A workspace is where you create repositories, collaborate on your code, and organize different streams of work in your Bitbucket Cloud account. Workspaces replace the use of teams and users in API cal
  name: Bitbucket Workspaces API
  phrasing_intents:
  - id: getUserPermissionsWorkspaces
    intent: List my workspace permissions (deprecated)
    question: Which workspaces am I in and what is my permission in each, via the older permissions endpoint?
  - id: getUserWorkspaces
    intent: List workspaces I can access
    question: What workspaces can I access, and am I an admin in any of them?
  - id: getUserWorkspacesByWorkspacePermission
    intent: Get my role in a workspace
    question: What is my highest level of access in a particular workspace?
  - id: getWorkspaces
    intent: List my workspaces (deprecated endpoint)
    question: Is there an older endpoint that lists workspaces filtered by my role?
  - id: getWorkspacesByWorkspace
    intent: Get a workspace
    question: What are the name, UUID and privacy of a workspace?
  - id: getWorkspacesByWorkspaceHooks
    intent: List a workspace's webhooks
    question: What webhooks fire for every repository in a workspace?
  - id: postWorkspacesByWorkspaceHooks
    intent: Create a workspace-wide webhook
    question: How do I get one webhook that fires for events in all repos of a workspace?
  - id: deleteWorkspacesByWorkspaceHooksByUid
    intent: Delete a workspace webhook
    question: How do I remove a webhook that fires for a whole workspace?
  phrasing_ops: 18
  slug: bitbucket-workspaces-api
- baseURL: https://api.bitbucket.org/2.0
  baseurl_source: declared
  description: 'Pull requests are a feature that makes it easier for developers to collaborate using Bitbucket. They provide a user-friendly web interface for discussing proposed changes before integrating them into '
  name: Bitbucket Pull Requests API
  phrasing_intents:
  - id: getPullrequestsForCommit
    intent: Find pull requests that contain a commit
    question: Which pull request was this commit reviewed and merged in?
  - id: getRepositoriesByWorkspaceByRepoSlugDefaultReviewers
    intent: List a repository's default reviewers
    question: Who gets added automatically as a reviewer on every new pull request in this repo?
  - id: deleteRepositoriesByWorkspaceByRepoSlugDefaultReviewersByTargetUsername
    intent: Remove a user from a repo's default reviewers
    question: How can I stop a person from being auto-added as reviewer on new pull requests?
  - id: getRepositoriesByWorkspaceByRepoSlugDefaultReviewersByTargetUsername
    intent: Check whether a user is a default reviewer
    question: Is a specific teammate already on the default reviewer list for a repo?
  - id: putRepositoriesByWorkspaceByRepoSlugDefaultReviewersByTargetUsername
    intent: Add a user to a repo's default reviewers
    question: How do I make someone review every new pull request in a repository automatically?
  - id: getRepositoriesByWorkspaceByRepoSlugEffectiveDefaultReviewers
    intent: List effective default reviewers incl. project
    question: Which default reviewers apply to a repo once the ones inherited from its project are included?
  - id: getRepositoriesByWorkspaceByRepoSlugPullrequests
    intent: List a repository's pull requests
    question: What pull requests are currently open on a Bitbucket repository?
  - id: postRepositoriesByWorkspaceByRepoSlugPullrequests
    intent: Open a new pull request
    question: How do I open a pull request from a feature branch into main?
  phrasing_ops: 37
  slug: bitbucket-pull-requests-api
artifact_total: 128
asyncapis:
- description: Bitbucket Cloud webhooks deliver event payloads to a subscriber URL via HTTP POST whenever a configured event occurs in a repository or workspace. Each event request includes an X-Event-Key header ide
  name: Bitbucket Cloud Webhook Events
  slug: bitbucket-cloud-webhooks-asyncapi
collections:
- collection_type: postman
  name: Bitbucket Addon API
  slug: postman-bitbucket-addon-api
- collection_type: postman
  name: Bitbucket Addon Branch restrictions API
  slug: postman-bitbucket-branch-restrictions-api
- collection_type: postman
  name: Bitbucket Addon Branching model API
  slug: postman-bitbucket-branching-model-api
- collection_type: postman
  name: Bitbucket Addon Commit statuses API
  slug: postman-bitbucket-commit-statuses-api
- collection_type: postman
  name: Bitbucket Addon Commits API
  slug: postman-bitbucket-commits-api
- collection_type: postman
  name: Bitbucket Addon Deployments API
  slug: postman-bitbucket-deployments-api
- collection_type: postman
  name: Bitbucket Addon Downloads API
  slug: postman-bitbucket-downloads-api
- collection_type: postman
  name: Bitbucket Addon GPG API
  slug: postman-bitbucket-gpg-api
- collection_type: postman
  name: Bitbucket Addon Issue tracker API
  slug: postman-bitbucket-issue-tracker-api
- collection_type: postman
  name: Bitbucket Addon Pipelines API
  slug: postman-bitbucket-pipelines-api
- collection_type: postman
  name: Bitbucket Addon Projects API
  slug: postman-bitbucket-projects-api
- collection_type: postman
  name: Bitbucket Addon properties API
  slug: postman-bitbucket-properties-api
- collection_type: postman
  name: Bitbucket Addon Pullrequests API
  slug: postman-bitbucket-pullrequests-api
- collection_type: postman
  name: Bitbucket Addon Refs API
  slug: postman-bitbucket-refs-api
- collection_type: postman
  name: Bitbucket Addon Reports API
  slug: postman-bitbucket-reports-api
- collection_type: postman
  name: Bitbucket Addon Repositories API
  slug: postman-bitbucket-repositories-api
- collection_type: postman
  name: Bitbucket Addon Search API
  slug: postman-bitbucket-search-api
- collection_type: postman
  name: Bitbucket Addon Snippets API
  slug: postman-bitbucket-snippets-api
- collection_type: postman
  name: Bitbucket Addon Source API
  slug: postman-bitbucket-source-api
- collection_type: postman
  name: Bitbucket Addon SSH API
  slug: postman-bitbucket-ssh-api
- collection_type: postman
  name: Bitbucket Addon Users API
  slug: postman-bitbucket-users-api
- collection_type: postman
  name: Bitbucket Addon Webhooks API
  slug: postman-bitbucket-webhooks-api
- collection_type: postman
  name: Bitbucket Addon Workspaces API
  slug: postman-bitbucket-workspaces-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bitbucket Addon API
  slug: open-bitbucket-addon-api
- collection_type: open
  name: Bitbucket Addon Branch restrictions API
  slug: open-bitbucket-branch-restrictions-api
- collection_type: open
  name: Bitbucket Addon Branching model API
  slug: open-bitbucket-branching-model-api
- collection_type: open
  name: Bitbucket API
  slug: open-bitbucket-cloud-rest-api
- collection_type: open
  name: Bitbucket Addon Commit statuses API
  slug: open-bitbucket-commit-statuses-api
- collection_type: open
  name: Bitbucket Addon Commits API
  slug: open-bitbucket-commits-api
- collection_type: open
  name: Bitbucket Addon Deployments API
  slug: open-bitbucket-deployments-api
- collection_type: open
  name: Bitbucket Addon Downloads API
  slug: open-bitbucket-downloads-api
- collection_type: open
  name: Bitbucket Addon GPG API
  slug: open-bitbucket-gpg-api
- collection_type: open
  name: Bitbucket Addon Issue tracker API
  slug: open-bitbucket-issue-tracker-api
- collection_type: open
  name: Bitbucket Addon Pipelines API
  slug: open-bitbucket-pipelines-api
- collection_type: open
  name: Bitbucket Addon Projects API
  slug: open-bitbucket-projects-api
- collection_type: open
  name: Bitbucket Addon properties API
  slug: open-bitbucket-properties-api
- collection_type: open
  name: Bitbucket Addon Pullrequests API
  slug: open-bitbucket-pullrequests-api
- collection_type: open
  name: Bitbucket Addon Refs API
  slug: open-bitbucket-refs-api
- collection_type: open
  name: Bitbucket Addon Reports API
  slug: open-bitbucket-reports-api
- collection_type: open
  name: Bitbucket Addon Repositories API
  slug: open-bitbucket-repositories-api
- collection_type: open
  name: Bitbucket Addon Search API
  slug: open-bitbucket-search-api
- collection_type: open
  name: Bitbucket Addon Snippets API
  slug: open-bitbucket-snippets-api
- collection_type: open
  name: Bitbucket Addon Source API
  slug: open-bitbucket-source-api
- collection_type: open
  name: Bitbucket Addon SSH API
  slug: open-bitbucket-ssh-api
- collection_type: open
  name: Bitbucket Addon Users API
  slug: open-bitbucket-users-api
- collection_type: open
  name: Bitbucket Addon Webhooks API
  slug: open-bitbucket-webhooks-api
- collection_type: open
  name: Bitbucket Addon Workspaces API
  slug: open-bitbucket-workspaces-api
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://www.atlassian.com/software/bitbucket/pricing
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bitbucket/refs/heads/main/plans/bitbucket-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bitbucket-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://bitbucket.org/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitbucket/refs/heads/main/capabilities/bitbucket-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bitbucket-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/bitbucket/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bitbucket/refs/heads/main/agentic-access/bitbucket-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bitbucket-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitbucket/refs/heads/main/security/bitbucket-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bitbucket-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitbucket/refs/heads/main/security/bitbucket-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bitbucket-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitbucket/refs/heads/main/security/bitbucket-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitbucket-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitbucket/refs/heads/main/authentication/bitbucket-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bitbucket-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitbucket/refs/heads/main/scopes/bitbucket-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/bitbucket-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/atlassian
- group: start
  title: ''
  type: Portal
  url: https://developer.atlassian.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.atlassian.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atlassian.com/legal/cloud-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atlassian.com/legal/privacy-policy
- group: start
  title: ''
  type: Signup
  url: https://bitbucket.org/account/signup/
- group: company
  title: ''
  type: Blog
  url: https://bitbucket.org/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atlassian
- group: operate
  title: ''
  type: Support
  url: https://support.atlassian.com/bitbucket-cloud/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bitbucket/refs/heads/main/json-ld/bitbucket-cloud-rest-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bitbucket-cloud-rest-api-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bitbucket/refs/heads/main/rules/bitbucket-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/bitbucket-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bitbucket/refs/heads/main/vocabulary/bitbucket-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/bitbucket-vocabulary.yaml
created: '2024-01-01'
description: Bitbucket is a Git-based source code repository hosting service owned by Atlassian offering both commercial plans and free accounts with unlimited private repositories, along with CI/CD pipelines, code reviews via pull requests, and code collaboration tools for development teams.
examples:
- key_count: 7
  name: Bitbucket Cloud Rest Api Commit Example
  slug: bitbucket-cloud-rest-api-commit-example
- key_count: 10
  name: Bitbucket Cloud Rest Api Pipeline Example
  slug: bitbucket-cloud-rest-api-pipeline-example
- key_count: 15
  name: Bitbucket Cloud Rest Api Pullrequest Example
  slug: bitbucket-cloud-rest-api-pullrequest-example
- key_count: 18
  name: Bitbucket Cloud Rest Api Repository Example
  slug: bitbucket-cloud-rest-api-repository-example
features:
- 'Free: 5 users, 1 GB, 50 build minutes/mo'
- 'Standard at $3.65/user/mo: unlimited users/storage, 2,500 build minutes'
- 'Premium at $7.25/user/mo: 3,500 minutes, AI PR, IP allowlisting, 99.9% SLA'
- REST API v2 at api.bitbucket.org/2.0
- 1,000 req/hr per user, 60K req/hr per IP
- Pipelines for CI/CD
- 'Pipeline concurrency: 1 Free, 10 Standard, 20 Premium'
- OAuth 2.0 + repository/workspace access tokens
- Webhooks for repository, PR, pipeline events
- Code insights for static analysis integration
- Self-hosted runners (1 slot Standard, 2 Premium)
- Deployment environments tracking
- Native Jira integration
- Atlassian Marketplace apps
- Git LFS support (5 GB Standard, 10 GB Premium)
- Forge / Connect framework for apps
finops:
- name: Bitbucket Finops
  service_category: Source Control + CI/CD
  slug: bitbucket-finops
image: /assets/icons/bitbucket.png
integrations:
- description: Deep integration with Jira for issue tracking and project management.
  name: Jira Software
- description: Connect Bitbucket with Trello for visual project management.
  name: Trello
- description: Receive Bitbucket notifications in Slack channels.
  name: Slack
- description: Link documentation in Confluence with code in Bitbucket.
  name: Confluence
- description: Deploy to AWS services using Bitbucket Pipelines.
  name: AWS
- description: Deploy to Azure services using Bitbucket Pipelines.
  name: Azure
- description: Deploy to Google Cloud using Bitbucket Pipelines.
  name: Google Cloud
- description: Build and push Docker images using Bitbucket Pipelines.
  name: Docker
json_schemas:
- name: Commit
  property_count: 7
  slug: bitbucket-cloud-rest-api-commit
- name: Pipeline
  property_count: 10
  slug: bitbucket-cloud-rest-api-pipeline
- name: Pullrequest
  property_count: 16
  slug: bitbucket-cloud-rest-api-pullrequest
- name: Repository
  property_count: 18
  slug: bitbucket-cloud-rest-api-repository
json_structures:
- name: Bitbucket Cloud Rest Api Commit Structure
  property_count: 4
  slug: bitbucket-cloud-rest-api-commit-structure
- name: Bitbucket Cloud Rest Api Pipeline Structure
  property_count: 6
  slug: bitbucket-cloud-rest-api-pipeline-structure
- name: Bitbucket Cloud Rest Api Pullrequest Structure
  property_count: 10
  slug: bitbucket-cloud-rest-api-pullrequest-structure
- name: Bitbucket Cloud Rest Api Repository Structure
  property_count: 15
  slug: bitbucket-cloud-rest-api-repository-structure
- name: Bitbucket Structure
  property_count: 0
  slug: bitbucket-structure
jsonld:
- class_count: 4
  name: Bitbucket Cloud Rest Api Context
  property_count: 23
  slug: bitbucket-cloud-rest-api-context
layout: provider
modified: '2026-05-29'
name: Bitbucket
nav: Providers
network: true
overview: 'Bitbucket publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Addon API, Branch restrictions API, Branching model API, and 20 more. Tagged areas include Atlassian, CI/CD, Code Collaboration, Code Review, and Developer Tools.


  The Bitbucket catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Bitbucket''s developer surface includes pricing, authentication, developer portal, signup flow, engineering blog, support, and 17 more developer resources.'
plans:
- name: Bitbucket Plans Pricing
  plan_count: 4
  slug: bitbucket-plans-pricing
- name: Bitbucket Price Estimates
  plan_count: 0
  slug: bitbucket-price-estimates
random_paper: 11
rate_limits:
- limit_count: 5
  name: Bitbucket Rate Limits
  slug: bitbucket-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Bitbucket API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: bitbucket-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Bitbucket API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bitbucket-jsonschema-spectral-rules
- effective_rule_count: 63
  extends:
  - spectral:oas
  name: Bitbucket API Rules
  rule_count: 22
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 12
  slug: bitbucket-spectral-rules
scopes:
- name: Bitbucket Scopes
  scope_count: 26
  slug: bitbucket-scopes
  summary_line: 26 scopes · authorizationCode
score:
  band: exemplar
  composite: 70.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 81.0
    catalog_earned_first_party: 12.0
    catalog_gap: 34.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 86.8
    contract_governance: 27.3
    contract_quality: 74.5
    developer_ergonomics: 39.3
    discoverability: 66.1
    operational_transparency: 26.3
  previous_composite: 70.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 43.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 100.0
screenshot: https://raw.githubusercontent.com/api-evangelist/bitbucket/refs/heads/main/screenshots/bitbucket-2026-06-20T173301.png
security:
- kind: authentication
  name: Bitbucket Authentication
  slug: bitbucket-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Bitbucket Domain Security
  slug: bitbucket-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bitbucket Vulnerability Disclosure
  slug: bitbucket-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Bitbucket Trust Center
  slug: bitbucket-trust-center
  summary_line: FedRAMP
slug: bitbucket
tags:
- Atlassian
- CI/CD
- Code Collaboration
- Code Review
- Developer Tools
- DevOps
- Git
- Pull Requests
- Repository Hosting
- Version Control
- Bitbucket
use_cases:
- description: Enforce code quality through structured pull request reviews with required approvals.
  name: Code Review Workflows
- description: Automate build, test, and deployment pipelines triggered by code changes.
  name: CI/CD Automation
- description: Enable distributed development teams to collaborate on code with workspaces and projects.
  name: Team Collaboration
- description: Manage releases with deployment tracking and environment promotion.
  name: Release Management
- description: Integrate security scanning into CI/CD pipelines for vulnerability detection.
  name: Security Scanning
website: https://bitbucket.org/
---

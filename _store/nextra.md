---
aid: nextra
url: https://raw.githubusercontent.com/api-evangelist/nextra/refs/heads/main/apis.yml
apis:
- aid: nextra:nextra
  name: Nextra
  tags:
  - Documentation
  - MDX
  - Next.js
  - Static Site Generator
  humanURL: https://nextra.site
  description: Nextra is the core Next.js plugin and library that provides MDX compilation, file-system page mapping, static image handling, search indexing, syntax highlighting, LaTeX support, and i18n utilities. It is consumed as a JavaScript/TypeScript package installed via npm and configured through the `nextra()` plugin in `next.config` files.
  properties:
  - url: https://nextra.site/docs
    type: Documentation
  - url: https://nextra.site/docs/guide
    type: GettingStarted
  - url: https://github.com/shuding/nextra
    type: GitHub
  - url: json-schema/nextra-config-schema.json
    type: JSONSchema
- aid: nextra:nextra-theme-docs
  name: Nextra Docs Theme
  tags:
  - Documentation
  - React
  - Theme
  humanURL: https://nextra.site/docs/docs-theme
  description: The Nextra Docs Theme (`nextra-theme-docs`) is a full-featured documentation theme built on top of the Nextra core. It provides a configurable sidebar with auto-collapse and nesting, a top navigation bar, a floating table of contents, dark mode toggle, edit-on-GitHub and feedback links, i18n language switching, next/prev page navigation, breadcrumbs, and a last-updated timestamp. Configuration is supplied as React props to the `` component.
  properties:
  - url: https://nextra.site/docs/docs-theme
    type: Documentation
  - url: https://nextra.site/docs/docs-theme/theme-configuration
    type: APIReferenceDocumentation
  - url: json-schema/nextra-theme-docs-config-schema.json
    type: JSONSchema
- aid: nextra:nextra-theme-blog
  name: Nextra Blog Theme
  tags:
  - Blog
  - Documentation
  - React
  - Theme
  humanURL: https://nextra.site/docs/blog-theme
  description: The Nextra Blog Theme (`nextra-theme-blog`) provides a minimal, clean blog layout built on Nextra. It supports post listings with tags and dates, RSS feed generation, and basic theming. Blog posts are written as MDX files under the `posts/` directory, and front matter fields such as `title`, `date`, `description`, and `tag` drive the post listing index.
  properties:
  - url: https://nextra.site/docs/blog-theme
    type: Documentation
  - url: https://github.com/shuding/nextra/tree/main/packages/nextra-theme-blog
    type: GitHub
name: Nextra
tags:
- Documentation
- MDX
- Next.js
- Open Source
- Static Site Generator
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Nextra is an open-source, Next.js-based documentation framework for building fast, modern, and beautifully styled documentation sites. It extends Next.js with MDX support, file-system routing, built-in search powered by Pagefind, syntax highlighting via Rehype Pretty Code, LaTeX rendering, static image optimization, i18n support, and a full-featured docs theme with sidebar, navbar, TOC, dark mode, and breadcrumb navigation.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


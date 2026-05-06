---
aid: css
url: https://raw.githubusercontent.com/api-evangelist/css/refs/heads/main/apis.yml
x-type: standard
name: CSS (Cascading Style Sheets)
description: Cascading Style Sheets (CSS) is a W3C web standard for describing the presentation of documents written in HTML and XML, including layout, colors, typography, and animations. CSS is a foundational web technology defined by the W3C CSS Working Group and is implemented natively by every major web browser. The CSS Object Model (CSSOM) and CSS Houdini extensibility APIs expose CSS to JavaScript at runtime.
tags:
  - CSS
  - Web Standards
  - W3C
  - Styling
  - Browser
type: Standard
specificationVersion: '0.19'
created: '2025-01-01'
modified: '2026-04-28'
apis: []
features:
  - name: Cascading and Inheritance
    description: Cascade, specificity, and inheritance rules combine author, user, and UA stylesheets.
  - name: Selectors
    description: Selectors Level 3/4 match elements by tag, class, id, attribute, structure, and state.
  - name: Box Model and Layout
    description: Block, inline, flex (Flexbox), and grid layout systems for composing pages.
  - name: Responsive Design
    description: Media Queries Level 3/4 enable layouts that adapt to viewport, capability, and user preferences.
  - name: Color and Typography
    description: CSS Color Levels 3-5 and CSS Fonts Level 3-4 define color spaces, gradients, and font features.
  - name: Animation and Transitions
    description: Keyframe animations, transitions, and motion paths driven entirely from stylesheets.
  - name: CSSOM
    description: The CSS Object Model exposes CSS rules and computed styles to JavaScript via DOM APIs.
  - name: CSS Houdini
    description: Low-level browser extensibility APIs (Paint, Layout, Properties and Values, Animation Worklet) for custom CSS behaviors.
useCases:
  - name: Web Page Styling
    description: Authors style HTML documents using stylesheets shipped with their site.
  - name: Responsive and Adaptive UI
    description: Apps adapt presentation to device, viewport, and user preferences (dark mode, reduced motion).
  - name: Component Libraries
    description: Design systems publish CSS-based components consumed by many applications.
  - name: Web Animations
    description: Marketing sites and apps animate UI states purely with CSS.
  - name: Browser Polyfills
    description: Houdini Paint and Layout worklets polyfill new CSS features in older browsers.
  - name: Accessibility
    description: Authors honor user preferences (prefers-reduced-motion, prefers-contrast) via media features.
common:
  - url: https://www.w3.org/Style/CSS/
    name: CSS at W3C
    type: Website
  - url: https://www.w3.org/TR/?tag=css
    name: CSS Specifications (W3C TR)
    type: Specifications
  - url: https://www.w3.org/Style/CSS/current-work
    name: CSS Current Work
    type: Documentation
  - url: https://www.w3.org/groups/wg/css/
    name: CSS Working Group
    type: Community
  - url: https://github.com/w3c/csswg-drafts
    name: CSSWG Drafts (GitHub)
    type: GitHubRepository
  - url: https://github.com/w3c/css-houdini-drafts
    name: CSS Houdini Drafts (GitHub)
    type: GitHubRepository
  - url: https://www.w3.org/TR/CSS22/
    name: CSS 2.2 Specification
    type: Specification
  - url: https://drafts.csswg.org/
    name: CSS Editor's Drafts
    type: Specifications
  - url: https://developer.mozilla.org/en-US/docs/Web/CSS
    name: MDN CSS Reference
    type: Reference
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

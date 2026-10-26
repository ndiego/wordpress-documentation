// Project configuration for the @wp-docs-toolkit/screenshots engine (wp-screenshots). Paths are relative to this file.
import { createRequire } from 'node:module';

// The toolkit's bundled demo site ("Saltmarsh", the Ipsum theme, a block showcase). Its README, in
// node_modules/@wp-docs-toolkit/demo-site/README.md, lists the slugs specs can rely on.
const demoSite = createRequire( import.meta.url ).resolve( '@wp-docs-toolkit/demo-site/blueprint.json' );

export default {
	specs: [ 'shots/**/*.yaml' ],
	outDir: '../docs/assets/screenshots',
	docsDir: '../docs',
	blueprint: demoSite,
	workDir: '.wp-screenshots',

	// Pinned environment. The demo site's blueprint `preferredVersions` is authoritative; keep both in sync.
	wordpress: { version: '7.1.3', php: '8.3' },
	port: 9400,

	format: 'webp',

	// The canonical render runs in this image. Keep it at the engine's @playwright/test version.
	dockerImage: 'mcr.microsoft.com/playwright:v1.64.0-noble',

	style: {},
};

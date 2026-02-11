"""Settings package that selects environment-specific overrides.

This file chooses the appropriate settings module based on environment
variables. It provides a heuristic to prefer production settings when the
app is running behind Render, where a preview URL is used.
"""

import os

# If PORTFOLIO_ENV is explicitly set, honor it. Otherwise, infer from Render.
ENV = os.environ.get('PORTFOLIO_ENV', None)
if ENV is not None:
    ENV = ENV.lower()
else:
    # Render preview usually exposes RENDER_EXTERNAL_HOSTNAME; prefer production
    # in that environment to avoid host-based 400s.
    ENV = 'production' if os.environ.get('RENDER_EXTERNAL_HOSTNAME') else 'development'

if ENV == 'production':
    from .production import *  # noqa
else:
    from .development import *  # noqa

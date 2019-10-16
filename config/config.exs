# This file is responsible for configuring your application
# and its dependencies with the aid of the Mix.Config module.
#
# This configuration file is loaded before any dependency and
# is restricted to this project.
use Mix.Config

# General application configuration
config :student_system,
  ecto_repos: [StudentSystem.Repo]

# Configures the endpoint
config :student_system, StudentSystemWeb.Endpoint,
  url: [host: "localhost"],
  secret_key_base: "8P/Zl8nl0UaPk0v7mGuCshUAw32MY6a8gzk2OkHQFY6abcZNQXgrEFaSfRApVKKG",
  render_errors: [view: StudentSystemWeb.ErrorView, accepts: ~w(html json)],
  pubsub: [name: StudentSystem.PubSub,
           adapter: Phoenix.PubSub.PG2]

# Configures Elixir's Logger
config :logger, :console,
  format: "$time $metadata[$level] $message\n",
  metadata: [:user_id]

# Import environment specific config. This must remain at the bottom
# of this file so it overrides the configuration defined above.
import_config "#{Mix.env}.exs"

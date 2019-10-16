defmodule StudentSystemWeb.PageController do
  use StudentSystemWeb, :controller

  def index(conn, _params) do
    render conn, "index.html"
  end
end

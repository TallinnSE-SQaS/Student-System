defmodule WhiteBreadContext do
  use WhiteBread.Context

  given_ ~r/^that I am not logged in to the SS$/, fn state ->
    {:ok, state}
  end

  and_ ~r/^I am user with details$/, fn state ->
    {:ok, state}
  end

  and_ ~r/^I go to the SS home page$/, fn state ->
    {:ok, state}
  end

  and_ ~r/^I enter my login details into the login form$/, fn state ->
    {:ok, state}
  end

  when_ ~r/^I submit the login form$/, fn state ->
    {:ok, state}
  end

  then_ ~r/^I should be redirected to my home page with the relevant information$/, fn state ->
    {:ok, state}
  end
end

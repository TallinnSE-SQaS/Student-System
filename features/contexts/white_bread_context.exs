defmodule WhiteBreadContext do
  use WhiteBread.Context
  use Hound.Helpers

  feature_starting_state fn  ->
    Application.ensure_all_started(:hound)
    %{}
  end

  scenario_starting_state fn _state ->
    Hound.start_session
    Ecto.Adapters.SQL.Sandbox.checkout(StudentSystem.Repo)
    Ecto.Adapters.SQL.Sandbox.mode(StudentSystem.Repo, {:shared, self()})
    %{}
  end

  scenario_finalize fn _status, _state ->
    Ecto.Adapters.SQL.Sandbox.checkin(StudentSystem.Repo)
    Hound.end_session
  end

  given_ ~r/^that I am not logged in to the Student System$/, fn state ->
    {:ok, state}
  end

  and_ ~r/^I am user with details$/, fn state, %{table_data: table} ->
    # table_data is a list of maps, each containing a row
    {:ok, state |> Map.put(:login_data, table)} # we'll have to save this data in the DB to actually test it
  end

  and_ ~r/^I go to the Student System home page$/, fn state ->
    navigate_to("/")
    {:ok, state}
  end

  and_ ~r/^I enter my login details into the login form$/, fn state ->
    [user_data|_] = state[:login_data]
    fill_field(:username, user_data[:username])
    fill_field(:password, user_data[:password])
    {:ok, state}
  end

  and_ ~r/^I try to login with username "(?<username>[^"]+)" and password "(?<password>[^"]+)"$/, fn state, %{username: username, password: password} ->
    {:ok, state |> Map.put(:username, username) |> Map.put(password, password)}
  end

  when_ ~r/^I submit the login form$/, fn state ->
    click(:submit)
    {:ok, state}
  end

  then_ ~r/^I should be redirected to my home page with the relevant information$/, fn state ->
    {:ok, state}
  end

  then_ ~r/^I should be back on the home page with an error message that reads "(?<message>[^"]+)"$/, fn state, %{message: message} ->
    {:ok, state}
  end

  # --- Enrolling into courses --- #

  given_ ~r/^I am logged in as a student$/, fn state ->
    {:ok, state}
  end

  and_ ~r/^I visit the page of a course called "(?<course_name>[^"]+)"$/, fn state, %{course_name: name} ->
    {:ok, state}
  end

  and_ ~r/^the course does not depend on other courses$/, fn state ->
    {:ok, state}
  end

  and_ ~r/^the course depends on "(?<course_name>[^"]+)"$/, fn state, %{course_name: name} ->
    {:ok, state}
  end

  and_ ~r/^the capacity of the course is (?<cap>\d+)$/, fn state, %{cap: cap} ->
    {:ok, state}
  end

  and_ ~r/^the number of enrolled students is (?<count>\d+)$/, fn state, %{count: count} ->
    {:ok, state}
  end

  when_ ~r/^I click on "(?<button_label>[^"]+)"$/, fn state, %{button_label: bt} ->
    {:ok, state}
  end

  then_ ~r/^I should be enrolled in the course$/, fn state ->
    {:ok, state}
  end

  then_ ~r/^I should see a message that reads, "(?<msg>[^"]+)"$/, fn state, %{msg: msg} ->
    {:ok, state}
  end

  and_ ~r/^the number of enrolled students should be (?<count>\d+)$/, fn state, %{count: count} ->
    {:ok, state}
  end

  and_ ~r/^the "(?<button_name>[^"]+)" button should be disabled$/, fn state, %{button_name: bt} ->
    {:ok, state}
  end
end

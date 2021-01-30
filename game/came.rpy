label came(times=1):
    $ plural = ""

    python:
        if times > 1:
            plural = "s"

    "I came here [times] time[plural]"

    return
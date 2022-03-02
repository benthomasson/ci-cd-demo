import os

from watchdog.events import RegexMatchingEventHandler
from watchdog.observers import Observer


def main(queue, args):

    root_path = os.path.abspath(args["path"])

    class Handler(RegexMatchingEventHandler):
        def __init__(self, **kwargs):
            RegexMatchingEventHandler.__init__(self, **kwargs)

        def on_created(self, event):
            print(event)
            queue.put(
                dict(
                    change="created",
                    src_path=event.src_path,
                    type=event.__class__.__name__,
                    root_path=root_path,
                )
            )

        def on_deleted(self, event):
            print(event)
            queue.put(
                dict(
                    change="deleted",
                    src_path=event.src_path,
                    type=event.__class__.__name__,
                    root_path=root_path,
                )
            )

        def on_modified(self, event):
            print(event)
            queue.put(
                dict(
                    change="modified",
                    src_path=event.src_path,
                    type=event.__class__.__name__,
                    root_path=root_path,
                )
            )

        def on_moved(self, event):
            print(event)
            queue.put(
                dict(
                    change="moved",
                    src_path=event.src_path,
                    type=event.__class__.__name__,
                    root_path=root_path,
                )
            )

    observer = Observer()
    handler = Handler(ignore_regexes=args.get("ignore_regexes"))
    observer.schedule(handler, root_path, recursive=args["recursive"])
    observer.start()

    try:
        observer.join()
    finally:
        observer.stop()
        observer.join()

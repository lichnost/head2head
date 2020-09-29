from .base_options import BaseOptions

class TestOptions(BaseOptions):
    def initialize(self):
        BaseOptions.initialize(self)
        self.parser.add_argument('--results_dir', type=str, default='./results/head2headDataset', help='saves results here.')
        self.parser.add_argument('--demo_dir', type=str, default=None, help='If not None, save the generated frames here, during demo.')
        self.parser.add_argument('--phase', type=str, default='test', help='train, val, test, etc')
        self.parser.add_argument('--time_fwd_pass', action='store_true', help='Show the forward pass time for synthesizing each frame.')
        self.parser.add_argument('--which_epoch', type=str, default='latest', help='which epoch to load? set to latest to use latest cached model')
        self.parser.add_argument('--do_reenactment', action='store_true', default=False, help='When set, perform source to target head reenactment and not self-reenactment.')
        self.parser.add_argument('--source_name', type=str, default=None, help='Name of source person. If None, test on all sources. Used only when do_reenactment is True.')
        self.parser.add_argument('--box_redetect_nframes', type=int, default=-1, help='Redetect face bbox every pointed frames')
        self.parser.add_argument('--realtime', action='store_true', default=True,
                                 help='Realtime fake video generation strait to fake web camera')
        self.parser.add_argument('--realtime_cam_id', type=int, default=1,
                                 help='Fake web camera id')
        self.isTrain = False
